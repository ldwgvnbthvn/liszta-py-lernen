# Loops
Loops are the core of programming and what makes programming useful, because something can be iterated without a human doing it for every data. 🥲

Kurzgesagt, there are **3 kinds of loops** in Py:
- For loop
- While loop
- Nested loop

## For loop
The `for` loop is used for iterating over a sequence (list, tuple, dictionary, set, and string).<br/>
Easy example: (this is used to print (command print can be replaced with other stuffs) every member of straw hats, uhm I mean member of a list. `Garp` can be any variable name. The list can be replaced by other collection type or even a string.
```python
mugiwara = ['Luffy','Zoro','Sanji']
for Garp in mugiwara:
  print(Garp)
```
Result:
```
Luffy
Zoro
Sanji
```
### For Break
`for` loop can be stopped before it has gone through all the items, by using `break` command.
```python
mugiwara = ['Luffy','Zoro','Sanji','Usopp','Nami']
for merry in mugiwara:
  print(merry)
  if merry == 'Sanji':
    break #don't forget the indentation
```
### For Continue
Unlike `break` which stops the entire process of the iteration, `continue` command skips the rest of the sequence loop (still continuing the current turn) and continues at the next line.<br/>
Example:
```python
mugiwara = ['Luffy','Zoro','Sanji','Usopp','Nami']
for merry in mugiwara:
  if merry == 'Sanji':
    continue
  print(merry)
```
### The range() Function in For Loop
`range()` is a function that returns sequences of numbers by a form of arithmetic progression. It needs starting number, increments value, and how many sequences.<br/>
For `range(x)`, `x` is the amount of numbers (before being "incremented"). Remember, Python index starts from zero. For example, if `x=6`, the values will be 0 to 5, not 0 to 6, with default increment of 1 and starting point of 0.<br/>
There is a more complete format: `range(x,y,z)`<br/>
`x` is starting number, `y` is amount of numbers (before "incremented"), `z` is increment number. Even though the starting point is from `x`, this is just the start point for "incrementing", not `y`. When counting `y`, we count from 0 (so the upper limit for incrementing will be `y-1`)
```python
for luffy in range(2,30,3):
  print(luffy) # will be 2, 5, 8, ... , 29 (remember 30 is counted from 0)
for zoro in range(5,10,3): # will be 5, 8
  print(zoro)
```
In `for` loop, `range()` is used to specify how many times looping will be done. `range()` function returns a sequence of numbers (default: start from 0, increments by 1), and ends at specified number.
```python
for luffy in range(2,6):
  print(luffy) # will be 2, 3, 4, 5 (remember 6 is counted from 0)
```

### For with else
It turns out that we can add `else` command too after the `for` loop, not only in `while` loop. With `else`, we can run some commands that only applies after the `for` loop is completely finished.
```python
for luffy in range(6):
  print(luffy)
else:
  print('DONE')
```

## While loop
The `while` loop is used for executing a set of commands as long as a certain condition is still True.
Easy example:
```python
Gear = 1
while Gear < 6:
  print(Gear)
  Gear += 2 #remember this increment to avoid looping forever
```
Result:
```
1
3
5
```
### While break and continue
These are similar to the `for` loop.

### While else
`else` can be added at the end to deal with situation when the condition is no longer true.  
```python
chopper = 1
while chopper < 6:
  print(x)
  i += = 1
else:
  print('chopper is no longer less than 6')
```


## Nested loop
Simply... nested loop is a loop inside a loop. The "inner" loop will be executed once for each interation of the "outer" loop. Let's start from nested `for` loop.
```python
# match every trait with each straw hat member
trait = ['fearless','clever']
mugiwara = ['Luffy','Zoro','Nami','Usopp','Sanji']
for merry in trait:
  for sunny in mugiwara:
    print(merry, sunny)
```
