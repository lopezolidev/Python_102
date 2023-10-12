# Higher Order Functions are functions that recieve another function as argument

def increment(x):
    return x + 1

def high_order_func(y, func):       # recieves the definition of the function and another value
    return y * func(y)  # the sent function is called with the value parameter as argument

result = high_order_func(3, increment)

print(result)   # 12

# we can also do the same with lambdas

increment_v2 = lambda x : x + 1

high_order_func_v2 = lambda y, func : y * func(y)

result_v2 = high_order_func_v2(5, increment_v2)

print(result_v2)        # 30


# this functions also can be substituted

result_v3 = high_order_func_v2(6, lambda w : w + 9) # we sent a raw definition of a lambda as the argument of the function 

print(result_v3)    # 90


