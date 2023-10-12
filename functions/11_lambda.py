# Lambda functions. A summarized form to write a function. A lambda function is a small anonymous function.

x = lambda y: y + 2 # ← recieves 'y', returns y + 2

print(x(3))     # 5


# also works will different arguments sent by commas
word = lambda letter1, letter2, letter3, letter4: letter1 + letter2 + letter3 + letter4

sentence = word('this ','is ','a ','sentence.')
print(sentence) # this is a sentence.

# strength of labdas is when you use them inside another function, then you create a "closure"

def my_func(n):
    return lambda x : x * n     # ← this function returns a function, that new function will have 2 as the multiplier 'n'

double = my_func(2)

print(double(3))    # 6 ← the 'x' is 3, and by how we declared it right above, now any number sent into the function will be multiplied by 2

# we can do the same but with more functions

def divider(m):
    return lambda x: x / m

half = divider(2)

third = divider(3)

print(half(4))      # 2.0
print(third(18))        # 6.0

# it's a some form of polymorphism

