# Set
- **Not** ordered
- Duplicate items are **not** allowed
- **Non**-changeable, but data can be added or removed
- If a set contains 2 items or moreof a same value, only 1 will be included
- The values False and 0 are considered the same value in sets and are treated as duplicates. The same thing applies to True and 1. <br/>
For example:
```python
this_set{'red','yellow','blue',False,True,0}
print(thisset)
```
will result `{False,True,'red','yellow','blue'}`

## Functions for SET
|Functions|Descriptions|Examples|
|---|---|---|
|`add()`|- Add an item to the set (**only 1 item**)|`my_set.update(['a'])`<br/>`my_set.update('a'.'b')` won't work|
|`update()`| - Add **multiple** items to the set<br/> - Can add items from other set or other type of collection|`my_set.update(['a','b'])`<br/>`my_set.update('a','b')`<br/>`my_set.update(my_list)`|
|`len()`|- Count number of items|`len(my_list)`|
|`remove()`|- Remove **only 1 item** from set (if item doesn't exist, will raise error)|`my_set.remove('b')`|
|`discard()`|- Remove **only 1 item** from set (if item doesn't exist, **won't** raise error)|`my_set.discard('b')`|
|`clear()`|- Make the set empty|`my_set.clear()`|
|`del`|- Delete the entire set|`del my_set`|
|`union()`|- Join two sets (not the violin one🌝) into 1 new set (won't include duplicates)|`c = setA.union(setB)`<br/>`all_set = setA.union(setB, setC)`|
|`update()`|- Modify 1 set to include all items from both sets (can't be assigned to other set)|`set_A.update(set_B)` (set_A will be updated with items from `set_B`<br/> Meanwhile, for `new_set = set_A.update(set_B)`, `new_set` will contain `None` and `set_A` will contain `set_A + set_B`|
|`set()`|- To make a set<br/> - Convert other collection type into set|`my_set = set(('a','b','c'))`<br/>`two_set = set(two_list)`|
|`copy()`|- Copy a set into other set (copy, not move)|`new_set = my_set.copy()`|
|`difference()`|- Return a set that contains the items that only exist in set A and not in set B|Set A and B will be used as example for the next functions in the table.<br/>`A = {'apple','grape','lemon'}`<br/>`B = {'google','apple','microsoft'}`<br/>`Y = A.difference(B,C)`<br/>`Z = A.difference(B)`<br/> Result: `Z = {'grape','lemon'}` and `A` is still the same|
|`difference_update()`|- Remove the item that exists in both set|`A.difference_update(B)`<br/>Result: `A = {'grape','lemon'}`|



