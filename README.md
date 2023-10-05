# Python_102
Study of python concepts such as Functions, Comprehensions, Errors and more

- - -

### Sets
- ##### [What are sets?](sets/01_sets.py)
	- Data structure where:
		- Values are modifiable 
		- Have no specific order
		- There're not repeated elements in the set (very much like the '[sets](https://en.wikipedia.org/wiki/Set_(mathematics))' from discreet math)
	- Are declared with '{}' and inside you type values separated with commas
- ##### [Modifying sets](sets/02_crud_sets.py)
	- **CRUD** process can be done in sets
		- Caveat with *'.remove'* and *'.discard'*, the former requires correct typing for not throwing an error, the latter handles such exception silently
- ##### [Operating sets](sets/03_ops_sets.py)
	- Basic operations of sets theory:
		- **Union**: set A  *OR*  set B → set C
		- **Intersection**: set A  *AND*  set B → set C
		- **Subtraction**: set A  *-*  set B (only elements shared by B) → set C
		- **Symmetric difference**: (set A  *OR*  set B)  *-* (set A  *AND*  set B) → set C

- - -

### Comprehensions
#### [What are lists comprehensions?](comprehensions/04_lists.py)
- *Comprehensions* refer to a form of creating abbreviated data structures. This concept in *lists* can be applied like:
```python
[element for element in iterable if condition]

# former "element" is the particular that will be added to the list
# "iterable" is the range or iterable data structure 
# "condition" refers to the barrier that the latter "element" will cross in order to become the latter "element", that being a part of the created list 
```
#### [What are dictionary comprehensions?](comprehensions/05_dict.py)
```python
{ key : value for value in iterable if condition }
```

- Also the function 'zip(list1, list2, list3...)' is useful for arranging various lists into a list of tuples:
```python
numbers = [1, 3, 6, 7, 8, 4, 3, 2]

letters = ['a', 'c', 'v', 'm']

bools = [True, True, False]

list(zip(numbers,letters,bools))

#using 'zip()' alone will return a pointer to the data structure, we must list it

[(1, 'a', True), (3, 'c', True), (6, 'v', False)]

#the resulting list is the size of the smaller list when sending lists of various lengths

```
#### [What are the conditions in dictionary comprehensions?](comprehensions/06_dictifs.py)
**Conditions** are "walls" to let some variable or element be inserted in the dictionary. In this case we can impose the condition to the key and the value.
Example:
```python
import random

countries = ['ven', 'col', 'pe', 'mx', 'br', 'arg']

  

population_v1 = {country: random.randint(1, 100) for country in countries} # ← creating a dictionary from a list using random numbers

print("population_v1: ", population_v1)

  

# population_v1: {'ven': 80, 'col': 32, 'pe': 54, 'mx': 20, 'br': 1, 'arg': 92}

  

# Adding the "if"

  

population_v2 = {country: population for (country, population) in population_v1.items() if population > 50}

print("population_v2: ", population_v2)

  

# population_v2: {'col': 63, 'br': 62, 'arg': 54}

# we used the function '.items()' to obtain a list of tuples of keys and values, then passed the conditional of greater than 50 to obtain only few elements

  

# Now using strings

  

text = "Hello, I am Sergio"

  

unique = {char: char.upper() for char in text if char in 'aeiou'} # ← each vowel found in the text will be transformed in upper case

print("unique: ", unique) 
# unique: {'e': 'E', 'o': 'O', 'a': 'A', 'i': 'I'}
```

#### List vs Sets vs Tuples

|              |**List** |**Tuple** |**Set** |
|--------------|---- |----- |----|
| *Mutable*        |✅  |❌    | ✅ |
| *Ordered*        | ✅ | ✅   | ❌ |
| *Indexing / Slicing* | ✅  | ✅   |❌ |
| *Duplicate elements*| ✅ | ✅   | ❌ |
