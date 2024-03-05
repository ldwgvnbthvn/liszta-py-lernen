# Tuple
- Immutable (CANNOT be changed after creation)
- Duplicates are allowed
- Ordered (has index)

I found this:<br/>
```python
my_tuple = ('Luffy','Nami','Franky','Robin','Sanji')
# For printing all members of the tuple
print(my_tuple[:])
# For selecting the 3rd index ([2]), and take the the 5th ([4]) character of the string
print(my_tuple[2][4])
```
Result: <br/>
```
('Luffy', 'Nami', 'Franky', 'Robin', 'Sanji')
k
```

## Functions for TUPLE
|Functions|Descriptions|Examples|
|---|---|---|
|```len()```|- Number of items in a tuple|```len(my_tuple)```|
|```+```|- Combine 2 or more tuples into a tuple|```tuple_Z = tuple_A + tuple_B + tuple_C```|
|```tuple()```|- Make a tuple<br/> - Convert other type of collection (like list) into tuple<br/> - Copy entire tuple into another tuple, whether that another tuple has something or not (```copy()``` command won't work with tuple, because tuples are NOT changeable)|```my_tuple = tuple(('a','b','c'))```<br/>```my_tuple = tuple(['a','b','c'])```<br/>```other_tuple = tuple(my_tuple)```|
|```count()```|- Count how many specified item|```n = name_tuple.count('Kevin')```|
|```index()```|- Returns index number of specified item<br/> If there are 2 or more same items, the index will be only the first one|```a = name_tuple.index('Kevin')```|
## Tips to change items in TUPLE
First, you have to convert the tuple into changeable collection like list. Then, make changes as needed and convert it back into tuple.<br/>
**Example:**
```python
x = ('k','m','s')
y = list(x)
y[2] = 'o'
x = tuple(y)
```
**The tuple ```x``` will be:**
```('k','m','o')```
