value = 100     # global scope → " everyone " can access this variable

def my_func():
    print(value)

my_func()   # 100

# --------------------------------------------------------------
'''
value2 = 200

def my_func_v2():
    value2 = value2 + 100   # this function has no "memory" about some "value2" variable, even though exists outside the function
    print(value2)

my_func_v2()    # UnboundLocalError: local variable 'value2' referenced before assignment   ← "value2" isn't accessible to the function
'''

# --------------------------------------------------------------

def my_func_v3():
    value = 200     # now the variable knows what is the variable "value"   ← Local scope
    value = value + 10  
    return value

print(value)    # 100
print(my_func_v3()) # 210


# Now let's apply local scope inside the function

def my_func_v4():
    value = 500
    result = value + 100        # ' result ' only exists inside the function, not outside → Local scope
    return result

print(my_func_v4()) # 600
# print(result)   # NameError: name 'result' is not defined ← ' result ' doesn't exists outside the function, therefore inaccessible