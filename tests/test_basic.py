from mycalculator import Calculator

def test_set_value():
    #Test initial setting for Calculator class
    assert Calculator().value == 0, "Object.value not set to default zero."
    assert Calculator(1.91).value == 1.91, "Object.value not set to correct value (1)."
    assert Calculator(-3.4).value == -3.4, "Object.value not set to correct value (2)."
    assert Calculator(-3.4).operation_log[0] == "Set value to -3.4", "Object.operation_log improperly initialized."

def test_add():
    #Test addition operation - add()
    test1 = Calculator(21)
    test2 = Calculator(-13.1)
    test1.add(12)
    test2.add(-2)
    assert test1.value == 33, "Operation add() did not perform correctly (1)."
    assert test2.value == -15.1, "Operation add() did not perform correctly (2)."
    
def test_subtract(): 
    #Test subtraction operation- substract()
    test1 = Calculator(33)
    test2 = Calculator(-15.1)
    test1.subtract(5)
    test2.subtract(23.1)
    assert test1.value == 28, "Operation subtract() did not perform correctly (1)."
    assert test2.value == -38.2, "Operation subtract() did not perform correctly (2)."
    
def test_multiply(): 
    #Test multiplication operation - multiply()
    test1 = Calculator(28)
    test2 = Calculator(-38.2)
    test1.multiply(10)
    test2.multiply(-2.2)
    assert test1.value == 280, "Operation multiply() did not perform correctly (1)."
    assert test2.value == 84.04, "Operation multiply() did not perform correctly (2)."
    
def test_divide(): 
    #Test division operation - divide()
    test1 = Calculator(280)
    test2 = Calculator(84.04)
    test1.divide(7)
    test2.divide(0.04)
    assert test1.value == 40, "Operation divide() did not perform correctly (1)."
    assert test2.value == 2101, "Operation divide() did not perform correctly (2)."

def test_root_1():
    #Test nth root operation - root()
    test = Calculator(16)
    test.root(4) #< Using Test 3
    assert test.value == 2, "Operation root() did not perform correctly (1)."

def test_logs():
    #Test log methods
    test = Calculator()
    test.add(5)
    test.subtract(2)
    assert len(test.operation_log) == 3, "Object.operation_log has incorrect length of elements (1)."
    assert test.operation_log[2] == "Subtract 2", "Object.operation_log has logged incorrect operation (1)."

def test_log_clear():
    #clear log
    test = Calculator()
    test.add(5)
    test.clear_log()
    assert len(test.operation_log) == 0, "Object.operation_log could not be cleared/reset (1)."

def test_reset_1():
    #Test reseting value - no additonal settings
    test = Calculator()
    test.add(5)
    test.subtract(2)
    test.reset()
    assert test.value == 0, "Object.value not reset to default zero."
    assert len(test.operation_log) == 4, "Object.operation_log could not be cleared/reset (2)."
    
def test_reset_2():
    #Test reseting value - set value, history == True
    test = Calculator()
    test.add(5)
    test.subtract(2)
    test.reset(5, history=True)
    assert test.value == 5, "Object.value not reset to correct value."
    assert len(test.operation_log) == 1, "Object.operation_log could not be cleared/reset (3)."
    