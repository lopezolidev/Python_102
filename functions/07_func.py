print("hello")  # hello

# declaring the function → reserved word "def"
def my_print():
    print("my print")

my_print()  # my print

# sending arguments to the function
def my_print_v2(text):
    print(text * 2)

my_print_v2('something...') # something...something...


my_print_v2(1)  # 2

# defining a function calling another function
def sum(a, b):
    my_print_v2(a + b)

sum(3, 8)   # 22
sum("hello", "world")   # helloworldhelloworld

# sum("hello", 2) # TypeError: can only concatenate str (not "int") to str