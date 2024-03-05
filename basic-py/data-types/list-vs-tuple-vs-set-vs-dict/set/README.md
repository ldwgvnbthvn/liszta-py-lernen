# Set
- **Not** ordered
- Duplicate items are **not** allowed
- **Non**-changeable, but data can be added or removed
- If a set contains 2 items or moreof a same value, only 1 will be included
- The values False and 0 are considered the same value in sets and are treated as duplicates. The same thing applies to True and 1.
<br/>
For example: <br/>
`this_set {'red','yellow','blue',False,True,0}`<br/>
`print(thisset)` will result `{False,True,'red','yellow','blue'}`

## Functions for SET
|Functions|Descriptions|Examples|
|---|---|---|
|`add()`|- Add an item to the set (**only 1 item**)|`my_set.update(['a'])`<br/>`my_set.update('a'.'b')` won't work|
|`update()`| - Add **multiple** items to the set<br/> - Can add items from other set or other type of collection|`my_set.update(['a','b'])`<br/>`my_set.update('a','b')`<br/>`my_set.update(my_list)`|
