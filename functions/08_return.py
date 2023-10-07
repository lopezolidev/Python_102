def my_func(a, b):
    print(a, b) # ← printing the arguments
    product = 0     # ← variable where the loop will iterate
    for x in range(a, b):       # ← for loop 
        product += a * b        # operation 
    return product          # return statement

my_func(3, 6)       # 3 6  ← only printed the print statement

result = my_func(3, 6)
print(result)       # 54

# sending the previous result as argument to the function
result = my_func(result, result * 2)
print(result)
# 54 108
# 314928














    