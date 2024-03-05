'''
~~~ LIST STUDIES ~~~
'''

# define a list
my_list = ["red", "yellow", "blue"]
my_list.append("green")
print(my_list)

my_list.insert(1, "orange")
print(my_list)


# del my_list without index will delete the entire list

del my_list[2]
print(my_list)
print(my_list[2])

my_list.remove("blue")
print(my_list)
my_list.pop()
print(my_list)
my_list.pop(0)
print(my_list)

del my_list

new_list = ["red","orange","yellow","green","blue","purple"]
old_list = ["grape","banana","apple","kiwi"]

#these two below will give the same result
#new_list = old_list.copy()
#new_list = list(old_list)

new_list = old_list.copy()
print(new_list)
print(old_list)

other_list = ["A","B","C","D","E"]
other_list.extend(new_list)
print(other_list)


multi_list = ["Alex","Kevin","Sebastian","Sam","Kevin","Arlo"]
x = multi_list.index("Kevin")
print(x)


sort_A = [1,3,5,2,4]
sort_A.sort()
print(sort_A)

multi_list.sort()
print(multi_list)


# If list contains both numbers and strings, it won'r sort
# mix_list = [5,'g',3,'d','c',2]
# mix_list.sort()
# print(mix_list)


list_decimal = [1.5, 0.3, 6.7]
list_decimal.sort()
print(list_decimal)


# convert a tuple into a list
A_tuple = ("a","b","c")
A_list = list(A_tuple)
print(type(A_list))


# Contidionals and Loops using list

num_list = [1,3,5,7,9]
char_list = ['Luffy','Zoro','Nami','Usopp','Sanji','Chopper', 'Robin']

# the water_7 and franky after for can be any name 
# (still follows variable name rules)
for water_7 in num_list:
    print('aye')

for franky in char_list:
    print(franky)

if 1 in char_list:
    print('Cola')
else:
    print('Tea')
    
if 'Robin' in char_list:
    print('Cola')
else:
    print('Tea')


last_list = ['a','b','c']
last_list[1] = 'x'
last_list[3] = 'y'
print(last_list)
# This won't work: last_list[1,2] = 'x','y'


