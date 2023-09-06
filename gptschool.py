
import os
import shutil
from flask import Flask, render_template, request, jsonify
import gpt_2_simple as gpt2

# Import TensorFlow
import tensorflow as tf

app = Flask(__name__)

# Update model_name to match the model size
model_name = "355M"

# Set the model directory based on your project directory
model_directory = os.path.join('/kaggle/input/gpt-project-school', 'models', model_name)

# Load the GPT-2 model only once (improves performance)
sess = None

def load_gpt2_model():
    global sess
    if sess is None:
        sess = gpt2.start_tf_sess()
        gpt2.load_gpt2(sess, model_name=model_name, model_dir=model_directory)

# Check for GPU availability
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    try:
        # Allow GPU memory growth (increases performance)
        tf.config.experimental.set_memory_growth(gpus[0], True)
    except RuntimeError as e:
        print(e)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.form['prompt']
    min_word_count = int(request.form['min_word_count'])  # Get the minimum word count from the request

    # Load the GPT-2 model only once
    load_gpt2_model()

    # Generate text until it reaches the minimum word count
    response = ""
    while len(response.split()) < min_word_count:
        text_chunk = gpt2.generate(sess, model_name=model_name, prefix=prompt, return_as_list=True)[0]
        response += text_chunk + " "

    return jsonify(response)

if __name__ == '__main__':
    app.run()

