--------------- Data Types --------------

integer = (1, 2, 3, etc)
float = (1.2, 3.2, etc.)
string = '' or ""
is_boolean = True or False
list = [   ] mutable Index - Starting from 0
tuple = ( ) immutabble Index - Starting from 0
my_dictionary = {1, 2, 3, etc.}
my_set = {1, 2, 3, 4, 5}
x = None - Absence of value
z = complex(3, 4) for j - -1 square root

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
(set1 | set2) - Union
(set1 & set2) - Intersection
(set1 - set2) - Difference - Just applies to Difference of set1 

--------------- Functions --------------

int(): converts a value to an integer.
float(): converts a value to a float.
str(): converts a value to a string.
bool(): converts a value to a boolean. 
len(): returns the length of a string or the number of elements in a list, tuple, or dictionary. Index - Starting from 0
max(): returns the maximum value in a list or tuple. Index - Starting from 0
min(): returns the minimum value in a list or tuple. Index - Starting from 0
sum(): returns the sum of all the elements in a list or tuple. Index - Starting from 0
type(): displays type of class inside data type.

-------------- Comparisons --------------

< -	strictly less than
<= - less than or equal
> - strictly greater than
>= - greater than or equal
== - equal
!= -not equal
is -object identity
is not -negated object identity

------------- Operations ----------------

x + y	sum of x and y	
x - y	difference of x and y	
x * y	product of x and y	
x / y	quotient of x and y	
x // y	floored quotient of x and y	1
3
5
6
x % y	remainder of x / y	2
3
-x	x negated	
+x	x unchanged	
abs(x)	absolute value or magnitude of x	
int(x)	x converted to integer	3
6
float(x)	x converted to floating point	3
6
complex(re, im)	a complex number with real part re, imaginary part im. im defaults to zero.	6
c.conjugate()	conjugate of the complex number c	
divmod(x, y)	the pair (x // y, x % y)	2
3
pow(x, y)	x to the power y	5
x ** y	x to the power y	5

-----------Observations --------------

Python also has the ability to perform arithmetic operations on variables of different data types. For example:
x = 5
y = 3.14
z = x + y
print(z)  # Output: 8.14

---------------------

#List modifier
list.append = add an Index
list.pop = remove an Index
#Tuple modifier
my_tuple = my_tuple + (4.4,)

------- I've found life representation ----------

try:
    i = 1
    while True:
        print(i)
        i += 1
except KeyboardInterrupt:
    print(“010 interrupted by 101”)
