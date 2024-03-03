# List
- For preserving sequence of data
- Need not to be homogenous all of time
- **Ordered**
- **Mutable** (can be changed after being created
- can contain duplicate items

## Functions for LIST
| Functions | Description | Example |
|---|---|---|
|```len()```| - How many elements a list have | ```len(my_list)```|
|```append()```|- Adds item to the last of the list <br/> - Can also be used for copying the list | ```my_list.append()```|
|```insert()```|- Adds item to a specific index|```my_list.insert(1,'red')```|
|```del```|- Deletes the entire list (no index indicated) <br/> - Delete items from specified index (index number indicated)|```del my list```</br>```my_list[2]```|
|```remove()```|- Removes the given item without knowing the exact index number|```my_list.remove('red')|
|```pop()```|- Removes the item from the specified index (or the last index if not specified)|```my_list.pop()```<br/>```my_list.pop(3)```|
|```copy()```|- To copy the content of a list into another list|```new_list = my_list.copy()```|
|```list()```|- Another way to define/make/create a list, without using [ ]<br/> - Can also be used to convert other type of collection (like tuple) into list <br/> - Can also be used to copy list like ```copy()``` function|```my_list = list(('a', 'b', 'c'))```<br/>```my_list = list(my_tuple)```<br/>```my_list = list(other_list)```|
|```extend()```|- Append a list with a content of another list|```A_list.extend(B_list)```<br/> The new A_list will be [content of A_list, content of B_list]|
|```+```|- Combine 2 or more lists into 1 list|```all_list = A_list + B_list + C_list```|
|```count()```|- Count how many specified item|```K = name_list.count('Kevin')<br/>N = grade_list.count(7)```|
|```index()```|- Returns index value of specified item<br/>- If there are 2 or more of the same items, the index will be only the first one in the list|```name_list = ['Kevin', 'Arlo', 'Kevin']```<br/>```x = name_list.index('Kevin')```<br/>```x``` will be 0, not 2|
|```sort()```| - Sort in ascending (from small to big, beginning to end) order. The list needs to contain only numbers (including floats) or only strings (not brass and woodwind), otherwise it won't work|```my_list.sort()```|
|```reverse()```|- Sort in descending order. (reverse order of ```sort()```)|```my_list.reverse()```|

## Combinations between conditionals and loops with LIST
Let's learn by examples. <br/>
```python
num_list = [1,3,5,7,9]
char_list = ["a","b","c","d","e","f"]

for water_7 in num_list:
    print("aye")

# the water_7 and franky after for can be any name* 
# *name that still follows variable name rules

for franky in char_list:
    print(franky)

if 1 in char_list:
    print("Cola")
else:
    print("Tea")
    
if 'Robin' in char_list:
    print('Cola')
else:
    print('Tea')
```
The output will be: <br/>
```
aye
aye
aye
aye
aye
Luffy
Zoro
Nami
Usopp
Sanji
Chopper
Robin
Tea
Cola
```




