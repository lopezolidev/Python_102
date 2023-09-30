# like discreet math sets, this data structure doesn't concieve repeated values, have no specific order and values are modifiable

set_countries = {'ven', 'col', 'mx', 'ven'}
print(set_countries)    # {'col', 'ven', 'mx'}
print(type(set_countries))  # <class 'set'>

# sets can vary in data type stored

set_numbers = {1, 0, 4, 4, 5, 89, 24, 786, 23204, 485, 0, 3, 969, 45, 784}
print(set_numbers)  # {0, 1, 3, 4, 5, 23204, 485, 969, 45, 784, 786, 24, 89}

# set_varied = {1, 'string', False, 99.9998, ['list1', 'list2']}
# print(set_varied)   # TypeError: unhashable type: 'list'  ← sets cannot print inner lists

set_varied = {1, 'string', False, 99.9998}      # ← only basic data types
print(set_varied)       # {False, 1, 99.9998, 'string'}

# we can obtain sets from other data structures

set_from_list = set(['a', 'b', 'c', 'd', 'f', 'd'])
print(set_from_list)    # {'f', 'c', 'b', 'd', 'a'}

set_from_tuple = set((3, 86, 123, 'abc', 'dd', True, False, False, 'abc', 86))
print(set_from_tuple)        # {False, True, 3, 'dd', 86, 'abc', 123}

set_dict = set({
    'name': 'John',
    'last_name': 'Doe'
})
print(set_dict)     # {'name', 'last_name'}  ← with dictionaries only takes the keys

set_from_string = set('heeeello')
print(set_from_string)      # {'l', 'h', 'o', 'e'}

numbers = [5, 3, 567, 4, 232, 3232, 323,232 , 2, 5, 6, 5, 5, 5, 7, 98, 98 ,455, 455, 1]
set_from_numbers = set(numbers)
print(set_from_numbers)     # {3232, 1, 2, 3, 4, 5, 323, 6, 232, 7, 98, 455, 567}

numbers_non_repeated = list(set_from_numbers)
print(numbers_non_repeated)     # [3232, 1, 2, 3, 4, 5, 323, 6, 232, 7, 98, 455, 567]  ← a list containing only the unique values

