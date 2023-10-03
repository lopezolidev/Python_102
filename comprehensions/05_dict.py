# "traditional" approach
dict = {}

for i in range(1, 5):
    dict[i] = i * 2

print("dict: ", dict)       # dict:  {1: 2, 2: 4, 3: 6, 4: 8}

# dictionary-comprehension

dict_v2 = {i: i*2 for i in range(1,5)}
print("dict_v2", dict_v2)       # dict_v2 {1: 2, 2: 4, 3: 6, 4: 8}

# example using random numbers, creating a dictionary from a list of countries
import random

countries = ['ven', 'col', 'cr', 'mx']

population = {}

for country in countries:
    population[country] = random.randint(20, 100)

print("population: ", population)       # population:  {'ven': 73, 'col': 22, 'cr': 52, 'mx': 100}


# Now using dictionary comprehensions

population_v2 = {country : random.randint(20, 100) for country in countries}
print("population_v2: ", population_v2)     # population_v2:  {'ven': 32, 'col': 60, 'cr': 20, 'mx': 63}


# now creating a dictionary from 2 lists

users = ['xavier', 'jackie', 'charlotte']

ages = [39, 23, 10]

print("only zip()", zip(users, ages))       # only zip() <zip object at 0x7f7144004180>  ← returns a pointer to such space in memory regarding that data structure

print("list of that pointer of zip(): ", list(zip(users, ages)))        # list of that pointer of zip():  [('xavier', 39), ('jackie', 23), ('charlotte', 10)]
# this is a list of tuples: [(name, age), (name, age), (name, age)]

# using dictionary comprehensions for this structure

users_data = {user : age for (user, age) in zip(users, ages)}
print("Users data: ", users_data) # Users data:  {'xavier': 39, 'jackie': 23, 'charlotte': 10}

# 1- transforming the list of users and ages into a list of tuples
# 2- resorting each pair of tuple where we identify the user and then the age
# 3- using key:value pair with each user and their respective age


# What happens when one list is shorter than the other?

numbers = [1, 3, 6, 7, 8, 4, 3, 2]
letters = ['a', 'c', 'v', 'm']

print("list(zip(numbers, letters)): ", list(zip(numbers, letters)))     # list(zip(numbers, letters)):  [(1, 'a'), (3, 'c'), (6, 'v'), (7, 'm')]

# the resulting list of tuples will be the size of the shorter list

# what happens when there're now 3 lists of different sizes each? 

bools = [True, True, False]

print("same but with 3 lists: ", list(zip(numbers, letters, bools)))        # same but with 3 lists:  [(1, 'a', True), (3, 'c', True), (6, 'v', False)]

# the resulting list will be of the size of the smaller list