# Package mycalculator 

## Introduction

The python package for "Calculator" class, which stores a number and provides basic math operations (e.g, add, subtract, multiply, divide, root). Values are cumulative and can be initially set and continually reset.

It provides five basic operations: 
> add, subtract, multiply, divide, root (nth)

Each function requires one number, which it will perform against the value stored within "value". In addition, all operations performed will be logged as a list "operation_log". The accumulative value can be reset.


## Basic Arithmetic Operations

There are 5 general arithmetic operations

- Addition - add()
- Subtraction - subtract()
- Multiplication - mutiply()
- Division - divide()
- Nth root - root()

Each method takes one number and performs the desired operation on the stored "value". 


For example, if the current value is 4, add(2) will add the number 2 to the value 4 and store the current total 6 as the new value. 

```python
from mycalculator import Calculator

compA = Calculator(4)
compA.add(2)
compA.value #< output: 6
```

Similarly, if the value is 27, root(3) will take the 3rd root of 27 which is 3.

```python
compA = Calculator(27)
compA.root(3)
compA.value #< output: 3
```

## Setting and resetting the current value

When creating an instance, the user can set the starting value (otherwise, default is 0).

```python
compA = Calculator(5)
compA.value #< output: 5
```

One can also reset the value using reset(). Similarly, a value can be provided or left to default of 0.

```python
compA = Calculator(5)
compA.reset()
compA.value #< output 0

compA.reset(324)
compA.value #< output 324
```

## Reviewing previous operations

History of performed operations are logged as a list and can be accessed under "operation_log".

```python
compA = Calculator(4)
compA.add(29)
compA.subtract(5)
compA.view_log() #< prints each operation by line, along with the current total
print(compA.operation_log) #< returns a list

# OUTPUT:
# Total Operations: 3
# Set value to 4
# Add 29
# Subtract 5
# Total: 28

# ['Set value to 4', 'Add 29', 'Subtract 5']

```

The log can be reset using clear_log() or during reseting of the cumulative total value.

```python
compA.clear_log() #Resets the log

compA.reset(history=True) #Resets the log, then changes value. (default is false)
```
