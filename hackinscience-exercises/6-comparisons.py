
# PROMPT: Find the biggest value in a given list.
# Try it by using only a temporary variable, a for loop, and an if to compare the values.

the_list = [
    143266561,
    1738152473,
    312377936,
    1027708881,
    1871655963,
    1495785517,
    1858250798,
    1693786723,
    374455497,
    430158267,
]

big = 0
for a in the_list:
    if a > big:
        big = a
    
print (big)