"""
Syntax of print:  
print(A, sep = B, end = C, file = D, flush = E)
A = thing(s) you want to print
B = the separator you want (MUST be string, default: space)
C = the end of what you want to print (MUST be string)
D = I'm still not sure what this is (will revise this when I understand what this is T_T)
E = boolean
if true, flushed
if false, buffered
(default: false)
"""
  
A = "apple"
B = "orange"
C = "mango"
# remember to put string between "" when defining variables
print(A)
  
"""
What appears on the console: 
>>> apple
"""



# You can also print directly, without calling the variables first
print("The world loves", " ", 42)
"""
>>>The world loves 42
Notice that the string and number are separated by a space,
because I don't define the separator and the default is a space.
"""

# Remember, separator and end must be a string
A = 1
B = 2
C = 3
print(A, B, C, sep="--", end="0")
"""
>>>1--2--30
"""
