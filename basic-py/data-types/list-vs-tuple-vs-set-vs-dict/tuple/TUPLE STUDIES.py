my_tuple = tuple(['a','b','c'])
print(type(my_tuple))

new_tuple = ('ha','hi','hu')
tuple_one = ('a','b','c')
tuple_two = (1,2,3)
new_tuple = tuple(tuple_one)
print(new_tuple)

name_tuple = ('Kevin','Arlo','Kevin')
k = name_tuple.index('Kevin')
print(k)
n = name_tuple.count('Kevin')
print(n)
# Apparently, the count function is still same as the list version


# CONDITIONALS AND LOOPS with TUPLE
num_tuple = (1,3,5,7,9)
char_tuple = ('Luffy','Zoro','Nami','Usopp','Sanji','Chopper', 'Robin')

# the water_7 and franky after for can be any name 
# (still follows variable name rules)
for water_7 in num_tuple:
    print('aye')

for franky in char_tuple:
    print(franky)

if 1 in char_tuple:
    print('Cola')
else:
    print('Tea')
    
if 'Robin' in char_tuple:
    print('Cola')
else:
    print('Tea')