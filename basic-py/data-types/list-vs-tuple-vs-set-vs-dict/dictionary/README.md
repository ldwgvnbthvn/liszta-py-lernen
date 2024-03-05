# Dictionary
- Contains **keys** and **values**
- Duplicate keys are NOT allowed
- Ordered (for Python 3.7) and Unordered (for Python 3.6 and older)
- Changeable
## Example of DICTIONARY
This is one way to define a dictionary:
```python
mydict = {
  'name':'Kevin',
  'year':1999,
  'likes':'music'
}
```
Dictionaries can also be written in one line like this:
```python
mydict = {'name':'Kevin','year':1999,'likes':'music'}
```
The name, year, and likes are **keys**.<br/>
The Kevin, 1999, and music are **values**.<br/>
<br/>
If a dictionary have a key that has two values such as:
```python
my_dict = {'color':'red','color':'yellow'}
```
`'color'` will only have one value. The last value of the same key will be used. So, `'color' = 'yellow'`
## How to add/replace a value of a certain key
This is how:<br/>
`my_dict['color'] = 'red'`<br/>
<br/>
Well...so I tried adding more than one keys and values at the same time.<br/>
`my_dict['color','shape'] = 'yellow','circle'`<br/>
It turns out that `'color','shape'` will be considered as one "tuple" key and `'yellow','circle'` will be considered as one "tuple" value.<br/>
The results: `my_dict = {('color','shape'):('yellow','circle')}`
## Functions for DICTIONARY
|Functions|Descriptions|Examples|
|---|---|---|
|`len()`|- Returns number of items in dictionary|`len(my_dict)`|
|`pop()`|- Deletes the item of specific item|`my_dict.pop('color')`|
|`popitem()`|- Removes last inserted item|`my_dict.popitem()`|
|`del`|- Deletes item of specific key<br/> - Deletes the entire dictionary|`del my_dict['color']`<br/>`del my_dict`|
|`clear()`|- Makes the dictionary empty|`my_dict.clear()`|
|`copy()`|- Copies the content of a dictionary into another dictionary (copy, not move)|`new_dict = my_dict.copy()`|
|`dict()`|- Another way to create a dictionary<br/> - Another way to copy dict like `copy()` function|`my_dict = dict(name = 'Kevin', year = 1999)`<br/>`mew_dict = dict(my_dict)`|
|`values()`|- Returns the values of a dictionary as `dict_values` class (can be converted into list or other type)|`x = my_dict.values()`<br/> The `x` will be `dict_values([value1,value2,...])`|
|`update()`|- Adds/replaces key(s) and their value(s)|`my_dict.update({'name':'Kevin'})`<br/>`my_dict.update({'name':'Kevin','year':1999})`<br/> Don't forget the **{ }**|
|`keys()`|- Returns all keys in a dictionary as `dict_keys` class (also can be converted into list or other type)|`key = my_dict.keys()`<br/> The `key` will be `dict_keys([key1,key2,...])`|
|`items()`|- Returns key-value couple as `dict_items` (that contains tuples inside a list)(can be converted, buat only the "outer" collection type)|`nani = my_dict.items()`<br/> `nani` will be `dict_items([(key1,key2,...),(value1,value2,...),...])`|
|`get()`|- Returns the value of specified key<br/> - Returns `None` if the key doesn't exist in the dictionary (the `None` can be changed into something else)<br/> (btw, `None`'s type is `NoneType`|`n = my_dict.get('name')`<br/>`n = my_dict.get('name,'kevin')`<br/>If `'name'` key doesn't exist , `n = 'Kevin'` not `n = None`|

