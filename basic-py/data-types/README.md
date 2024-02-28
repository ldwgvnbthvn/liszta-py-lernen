# DATA TYPES IN PYTHON
| Data types | Examples |
| --- | --- |
| Text type | ```str``` |
| Numeric type | ```int```, ```float```, ```complex``` |
| Sequence type | ```list```, ```tuple```, ```range``` |
| Mapping type | ```dict``` |
| Set type | ```set```, ```frozenset``` |
| Boolean type | ```bool``` |
| Binary type | ```bytes```, ```bytearray```, ```memoryview``` |
| None type | ```NoneType``` |

To check the type: use ```type()```
Example:
``` 
x = 5
print(type(x))
```

```str``` = text as usual

```int``` = integers (bilangan bulat)

```float``` = decimals

```complex``` = complex number and scientific notations (2.5E-2 = 0.025 = 2.5*10^(-2))

How to write complex numbers:
```python
# needs to import this
import cmath
# initializing complex number
z = 3+5j
# another way to initialize complex number
a = 7
b = 8
y = complex(a,b);
# print real and imaginary part of complex number
print('real of z is ', z.real)
print('imaginary of z is ', z.imag)
print('real of y is ', y.real)
print('imaginary of y ', y.imag)
```

```range``` = series of sequential integers begins from 0, with increments of 1, for example: 0, 1, 2, 3, ... 

```list```, ```tuple```, ```set```, ```frozenset```, and ```dict``` needs a different page to explain the differences between them. This will be in data structure section.

```bool``` = boolean, only True or False (with capital T and F)

Still not sure about ```bytes```, ```bytearray```, and ```memoryview```. Will come back to these later.

```NoneType``` = object that indicates no value

