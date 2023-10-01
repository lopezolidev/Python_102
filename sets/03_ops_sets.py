# Let's do some basic operations from set theory

set_a = {'ven', 'col', 'us'}
set_b = {'ven', 'pe', 'br'}

# Union: elements in A OR elements in B → set C

set_c = set_a.union(set_b)
print(set_c)        # {'col', 'br', 'pe', 'ven', 'us'}
print(set_a | set_b)     # {'col', 'br', 'pe', 'ven', 'us'}   

# Intersection: elements in A AND elements in B → set C
set_c = set_a.intersection(set_b)
print(set_c)        # {'ven'}
print(set_a & set_b)        # {'ven'}

# Substraction: elements in A - SHARED elements in B → set C (elements of A without the elements shared by B)
set_c = set_a.difference(set_b)
print(set_c)        # {'us', 'col'}
print(set_a - set_b)        # {'us', 'col'}
set_c = set_b.difference(set_a)
print(set_c)        # {'pe', 'br'}
print(set_b - set_a)        # {'pe', 'br'}

# Symmetric difference: (elements in A OR elements in B) - elements in A AND elements in B → set C
set_c = set_a.symmetric_difference(set_b)
print(set_c)        # {'us', 'pe', 'br', 'col'}
print((set_a | set_b) - (set_a & set_b))        # {'us', 'pe', 'br', 'col'}
print(set_a ^ set_b)           # {'us', 'pe', 'br', 'col'}

