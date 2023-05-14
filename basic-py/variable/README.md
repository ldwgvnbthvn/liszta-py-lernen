# Rules for naming Python variables:
- Must start with a letter or underscore character (Acceptable: `_hi5`)
- Can't start with a number (Wrong example: `5_var`)
- Can only contain letters (upper and lowercase), numbers (0-9) and underscore
- Variable names are case-sensitive (dnd, DnD, and DND are different variables)
  
# How to define variable in py:  
You don't need a command (unlike in SQL and other languages) to define a variable. You just need to use `=` to define it. 
  
Example: `A = 145`  
That's it! You made a variable.
  
# Types of Variables  
There are 4 types of variables:  
- Numbers
- String
- List
- Tuple
- Dictionary 
  
In this section, I won't explain the list, tuple, and dictionary because I will explain them in the array section. They are very long to explain and I need space 🥴  
  
## NUMBERS
There are 4 types of numbers:  
- int (integer)  
int doesn't have a limit (only limited by available memory of the device you have)
Example: `10, 100, 12763, -2982`  
- long int (a veryyyy loooooong integer)  
This type only exists in Python 2.7. In Python 3, the long int is also called the integer.  
- float (basically a decimal, including notation using exponential)  
Example: `0.1, -0.245, -23.4e100, 14.4-E14`  
- complex (use j for imaginary unit instead of i, including a float and exponential complex)  
Example: `3.14j, 25j, 5231+0j, 34.353-23j, 4e23+13j, 4.24e+3j`  
  
**Hint:** If you need a very big number, you can use "inf".  

## STRING
String is a set of characters, ANY characters. String is written between single or double quotation marks. (personally, I prefer using double, even though I need to press shift)  
Example:  
```
A = "Hey hey heyyy"
B = 'said Bokuto'
C = "@%$&#^%$!!!"
```
**How to know the type of a variable**  
Use `type()` function.  
```
a = 15
b = "Beethoven"
print(type(a))
print(type(b))
```
The output:  
<class 'int'>  
<class 'str'>
