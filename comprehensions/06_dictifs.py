# Applying dictionary comprehensions with conditionals

numbers = {}

for number in range(1,20):
    if(number % 3 == 0):
        numbers[number] = number / 3

print("numbers: ",numbers)
# numbers:  {3: 1.0, 6: 2.0, 9: 3.0, 12: 4.0, 15: 5.0, 18: 6.0}

# Now with the dictionary comprehension

numbers_v2 = {number : number / 3 for number in range(1, 20) if number % 3 == 0}
print("numbers_v2: ", numbers_v2)

# numbers_v2 {3: 1.0, 6: 2.0, 9: 3.0, 12: 4.0, 15: 5.0, 18: 6.0}

# Now using countries (list), then turning it into a dictionary and this last into another dictionary as example

import random
countries = ['ven', 'col', 'pe', 'mx', 'br', 'arg']

population_v1 = {country: random.randint(1, 100) for country in countries}  # ← creating a dictionary from a list using random numbers
print("population_v1: ", population_v1)

# population_v1:  {'ven': 80, 'col': 32, 'pe': 54, 'mx': 20, 'br': 1, 'arg': 92}

# Adding the "if"

population_v2 = {country: population for (country, population) in population_v1.items() if population > 50}
print("population_v2: ", population_v2)

# population_v2:  {'col': 63, 'br': 62, 'arg': 54}

# we used the function '.items()' to obtain a list of tuples of keys and values, then passed the conditional of greater than 50 to obtain only few elements

# Now using strings

text = "Hello, I am Sergio"

unique = {char: char.upper() for char in text if char in 'aeiou'} # ← each vowel found in the text will be transformed in upper case
print("unique: ", unique)   # unique:  {'e': 'E', 'o': 'O', 'a': 'A', 'i': 'I'}

# Let's do the same but with the frequency
