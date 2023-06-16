# -*- coding: utf-8 -*-
"""Calculator class stores a number, and performs simple arithmetic operations
Author: Jesse Huang
Date last updated: 2023-06-15
Date Created: 2023-06-14
"""

class Calculator:
    """Calculator: a basic arithmetic calculator
    It stores a single float number (which can be pre-set) and allows 
    users to perform basic accumulative arithmetic operations on it.
    
    It provides five basic operations: 
        > add, subtract, multiply, divide, root (nth)
        
    Each function requires one number, which it will perform against the 
    value stored within "value". In addition, all operations performed 
    will be logged as a list "operation_log". Accumulative value can be reset.
    """
    
    def __init__(self, value: float = 0):
        self.value = value
        self.operation_log = [f"Set value to {value}"]
    
    def __repr__(self):
        return f"{type(self).__name__}(value={self.value})"
    
    def __str__(self):
        return f"{{Total: {self.value}, Operations: {len(self.operation_log)}}}"
    
    # Basic arithmetic operations
    def add(self, num: float) -> None:
        """Operation: Add number to total"""
        self.value += num
        self.operation_log.append(f"Add {num}")
        
    def subtract(self, num: float) -> None:
        """Operation: Subtract number from total"""
        self.value -= num
        self.operation_log.append(f"Subtract {num}")
        
    def multiply(self, num: float) -> None:
        """Operation: Multiple total by number"""
        self.value *= num
        self.operation_log.append(f"Multiply by {num}")
        
    def divide(self, num: float) -> None:
        """Operation: Divide total by number"""
        self.value /= num
        self.operation_log.append(f"Divide by {num}")
    
    def root(self, num: int) -> None:
        """Operation: Calculate nth root of current total"""
        self.value = self.value**(1/num)
        self.operation_log.append(f"Calculate the {num}th root")

    # Operation log methods
    def view_log(self) -> None:
        """Print log of all operations"""
        print(f"Total Operations: {len(self.operation_log)}")
        print(*self.operation_log, sep="\n")
        print(f"Total: {self.value}")
        
    def clear_log(self) -> None:
        """Reset log of all operations"""
        self.operation_log = []
        
    # Additional non-operation methods
    def reset(self, value: float = 0, history: bool = False) -> None:
        """Reset accumulative total for the calculator"""
        if history: self.clear_log() # Reset operations log, if requested
        self.value = value
        self.operation_log.append(f"Set value to {value}")
