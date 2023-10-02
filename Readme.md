------------ Java -------------

Java runs OOPs ( Object Oriented Programming)

If we have to assign a value to float, we must add an ‘f’ at the end of the number

javac "Java File name" - "HelloWorld.java"

----------------- Arithmetic operators ---------------------
+ 	add
- 	subtract
/ 	divide
* 	multiply
% 	modulus division
++ 	post and pre-increment
-- 	post and pre-decrement
  	
-------------- Comparative operators -------------
< 	Less than
> 	Greater than
<= 	Less than or equal to
>= 	Greater than or equal to
== 	Equal to
!= 	Not equal to

------------ Boolean operators ------------------

! 	Boolean NOT - inverts boolean
&& 	Boolean AND - both boleans True
|| 	Boolean OR - one or other bolean True
^ 	Boolean exclusive XOR - If one is True, output True.

----------------- Unary operators ----------------------------

+ , -  - 	Unary Plus and minus 	Right to left
! , ~ 	Logical NOT and bitwise NOT 	Right to left
= 	Direct assignment 	Right to left
+= , -= 	Assignment by sum and difference 	Right to left
*= , /= , %= 	Assignment by product, quotient, and remainder 	Right to left
<<= , >>= 	Assignment by bitwise left shift and right shift 	Right to left
&= , ^= , = 	Assignment by bitwise AND, XOR, and OR 	Right to left
++ , -- 	Suffix/postfix increment and decrement 	Right to left
* , / , % 	Multiplication, division, and remainder 	Left to Right
+ , - 	Addition and subtraction 	Left to Right
<< , >> 	Bitwise left shift and right shift 	Left to Right
< , <= 	For relational operators 	Left to Right
> , >= 	For relational operators 	Left to Right
== , != 	For relational 	Left to Right
& 	Bitwise AND 	Left to Right
^ 	Bitwise XOR (exclusive or) 	Left to Right
&& 	Logical AND 	Left to Right
|| 	Logical OR 	Left to Right
| 	Bitwise OR (inclusive or) 	Left to Right

------------- MATH ---------------------

---------------- Exponentiation ---------------

public class exponent {
    public static void main(String[] args) {
        System.out.println("2 raised to the power 3 is " + Math.pow(2, 3));
        System.out.println("Exponent squared is " + Math.exp(2));
        System.out.println("The square root of 16 is " + Math.sqrt(16));
        System.out.println("The cube root of 27 is " + Math.cbrt(27));

--------------- Logarithms -----------------

  public class exponent {
    public static void main(String[] args) {  
        System.out.println("log of 2 is " + Math.log(2));
        System.out.println("log to the base 10 of 100 is " + Math.log10(100));

-------------- Trigonometry -----------------

  public class exponent {
    public static void main(String[] args) {   
        System.out.println("tan(45) =" + Math.tan(Math.toRadians(45)));
        System.out.println("sin(45) =" + Math.sin(Math.toRadians(45)));
        System.out.println("cos(45) =" + Math.cos(Math.toRadians(45)));

  //The method Math.toRadians() converts a degree number to a radian number and Math.toDegrees() does vice versa.

-------------- Absolute value --------------- 

  public class exponent {
    public static void main(String[] args) { 
        System.out.println("Absolute value of 2: " + Math.abs(2));


-------------- Maximum and minimum values --------------- 

   public class exponent {
    public static void main(String[] args) { 
        System.out.println("Maximum between 2.04 and 2.05: " + Math.max(2.04, 2.05));
        System.out.println("Minimum between 2 and 23: " + Math.min(2, 23));


------------------------


    Write a Java program to print your name to the console.

java
public class Exercise1 {
    public static void main(String[] args) {
        System.out.println("Your name");
    }
}

    Write a Java program to print your age to the console.

java
public class Exercise2 {
    public static void main(String[] args) {
        int age = 25; // Replace 25 with your age
        System.out.println("Your age is " + age);
    }
}

    Write a Java program to print the sum of two numbers to the console.

java
public class Exercise3 {
    public static void main(String[] args) {
        int num1 = 10;
        int num2 = 20;
        int sum = num1 + num2;
        System.out.println("The sum of " + num1 + " and " + num2 + " is " + sum);
    }
}

    Write a Java program to print the difference between two numbers to the console.

java
public class Exercise4 {
    public static void main(String[] args) {
        int num1 = 20;
        int num2 = 10;
        int diff = num1 - num2;
        System.out.println("The difference between " + num1 + " and " + num2 + " is " + diff);
    }
}

    Write a Java program to print the product of two numbers to the console.

java
public class Exercise5 {
    public static void main(String[] args) {
        int num1 = 5;
        int num2 = 10;
        int product = num1 * num2;
        System.out.println("The product of " + num1 + " and " + num2 + " is " + product);
    }
}

    Write a Java program to print the result of dividing two numbers to the console.

java
public class Exercise6 {
    public static void main(String[] args) {
        int num1 = 20;
        int num2 = 5;
        int quotient = num1 / num2;
        System.out.println("The quotient of " + num1 + " and " + num2 + " is " + quotient);
    }
}

    Write a Java program to declare a variable of type 'int' and assign it a value of 10. Then, print the value of the variable to the console.

java
public class Exercise7 {
    public static void main(String[] args) {
        int num = 10;
        System.out.println("The value of num is " + num);
    }
}

    Write a Java program to declare a variable of type 'double' and assign it a value of 3.14. Then, print the value of the variable to the console.

java
public class Exercise8 {
    public static void main(String[] args) {
        double num = 3.14;
        System.out.println("The value of num is " + num);
    }
}

    Write a Java program to declare a variable of type 'String' and assign it a value of "Hello World!". Then, print the value of the variable to the console.

java
public class Exercise9 {
    public static void main(String[] args) {
        String message = "Hello World!";
        System.out.println(message);
    }
}

    Write a Java program to take input from the user and print it to the console.

java
import java.util.Scanner;

public class Exercise10 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter your name: ");
        String name = input.nextLine();
        System.out.println("Your name is " + name);
    }
}

