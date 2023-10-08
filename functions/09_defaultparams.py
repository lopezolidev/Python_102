def calculate_volume(width = 1, length = 1, height = 1):  # ← default parameters equal to 1
    if(width > 0 and length > 0 and height > 0):
        return width * length * height
    
result = calculate_volume()
print(result)   # 1

result = calculate_volume(3, 9, 2)
print(result)   # 54

# if we want to send a specific value

result = calculate_volume(length = 32)
print(result)   # 32

# works with more than 1 value

result = calculate_volume(width = 30, length = 8)
print(result)   # 240

# Multiple returns

def tell_me_stories(phrase1 = 'some ', phrase2 = 'magic ', phrase3 = 'road...'):
    return phrase1 + phrase2 + phrase3, phrase2, phrase3        # separating by commas the different returns

result = tell_me_stories()
print(result)   # ('some magic road...', 'magic ', 'road...')   ← return a tuple

result, second, last = tell_me_stories()
print(result, second, last)     # some magic road... magic  road...

# if we want the result in form of a list
result = list(tell_me_stories('first', 'second', 'last'))
print(result) # ['firstsecondlast', 'second', 'last']