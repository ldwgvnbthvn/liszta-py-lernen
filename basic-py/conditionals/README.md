# Conditionals
There are several logical conditions that can be used to make statement in Py.
| Condition | Symbol |
|---|---|
| Equal | `a == b` |
|Not equal|`a != b`|
|Less than|`a < b`|
|Less than or equal to|`a <= b`|
|Greater than|`a > b`|
|Greater than or equal to|`a >= b`|

Logical operators are also can be used in statements. There are 3 basic logical operators:<br/>
- `AND` = both of the conditions have to be True so that the whole statement is True.
- `OR` = only one of the conditions that have to be True so that the whole statement is True.
- `NOT` = the opposite condition have to be True so that the whole statement is True.

Here are truth table for `AND`, `OR`, and `NOT`:
|A|B|AND|OR|NOT(A)|NOT(B)|
|---|---|---|---|---|---|
|T|T|T|T|F|F|
|T|F|F|T|F|T|
|F|T|F|T|T|F|
|F|F|F|F|T|T|

There are **4** types of conditionals:
- If statement
- If-Else statement
- If-Elif-Else statement
- Nested if statement

Before jumping into those conditionals, here are some **anti-syntax-frustration tips** on Py conditionals:
- Make sure your conditionals are in lowercase (`if` and `else` instead of `If` and `Else`). Remember, Py is case-sensitive. At one time, I spent half hour finding out why I got syntax error on a very simple conditional practice, it turns out it was this simple problem 😔.
- Put `:` after putting your conditions. The `:` has meaning that this line has some "operations" inside. 
- Don't forget to put tab before the actions after the conditional. These tabbed lines are the "operations".
- For condition "if something equals something" format, use `==` instead of `=`. These two are different. `=` is used to define a variable, while `==` literally means equal.

## If Statement
If this condition is true, do something. If this condition is not true, do nothing and move on to the next thing.<br/>
```python
k = 20
if k > 22:
    print("Oh no I'm getting old")
print('They said age is only number')
```

## If-Else Statement
If A condition is NOT true, try B condition first. 
```python
#Type your answer here.
name= input('Please input your name')
if name == 'Bond':
    print('Welcome on board 007')
else:
    print('Good Morning ',name)
```

## If-Elif-Else Statement
If A condition is NOT true, try B condition. If still not true, try C conditions, etc. Elif statements can be stacked.<br/>
Elif statement is like a prince going to a village and knocking on every villager's door to find a beautiful suitor (beautiful can also be from the inside💖). He had a certain standard for a beautiful suitor, so whenever he found a villager under his standard, he would knock another door. If he knocked the `else` door and he still didn't find any suitor that meet his standard... well maybe his soulmate is in another village/town.
```python
char = 'Chopper'
if char == 'Luffy':
    print('gomu')
elif char == 'Usopp':
    print('sogeking')
elif char == 'Zoro':
    print('onigiri')
elif char == 'Robin':
    print('fleur')
elif char == 'Franky':
    print('Cola')
else:
    print('rumble')
```

## Nested If Statement
This is different from elif statement. Nested if statement is like extra security doors that guests need to go through to meet the king 👑 and not every guest can be allowed to meet the king 👑. Only guest that meet all requirements can pass all the doors and meet the king 👑
```python
numbers = [1,3,4,6,7,8,9,12]

# Make for loop
for luffy in numbers:
    # Condition 1: is the number is odd?
    if luffy%2 != 0:
        # Condition 2: is the number a multiple of 3?
        if luffy%3 == 0:
            print(luffy, 'is an odd number and a multiple of 3')
# Long live king of pirates
```

 
