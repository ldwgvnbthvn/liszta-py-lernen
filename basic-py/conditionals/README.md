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
If this condition is true, do something.<br/>
```python
#Type your answer here.
name= input('Please input your name')
if name == 'Bond':
    print('Welcome on board 007')
else:
    print('Good Morning ',name)
```

## If-Else Statement
If A condition is NOT true, try B condition first. 
## If-Elif-Else Statement
If A condition is NOT true, try B condition. If still not true, try C conditions, etc. Elif statements can be stacked.
## Nested If Statement
asdf

 
