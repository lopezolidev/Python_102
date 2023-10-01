set_countries = {'ven', 'col', 'mx', 'br'}

# count elements in the set
print(len(set_countries))       # 4

# to know if some element is in the set
print('pe' in set_countries)        # False
print('ar' in set_countries)        # False
print('ven' in set_countries)       # True

# -----------------------------

# add 
set_countries.add('pe')
print(set_countries)    # {'ven', 'pe', 'br', 'mx', 'col'}
set_countries.add('pe')
print(set_countries)        # {'ven', 'pe', 'br', 'mx', 'col'}

# set_countries.add('ar', 'ecua')
# print(set_countries)        # TypeError: set.add() takes exactly one argument (2 given)  ← only 1 argument permitted

# -----------------------------

# update
set_countries.update({'col', 'pe', 'ar', 'ecua', 'uru'})      # ← sending another set to sum it in the previous set
print(set_countries)        # {'uru', 'ar', 'mx', 'ecua', 'col', 'br', 'pe', 'ven'}     ← no countries repeat

# -----------------------------

# remove

#set_countries.remove('arg') # typing wrongly on purpose
#print(set_countries)        # KeyError: 'arg'   ← '.remove' works if and only if the element is typed correctly, if not an error will be thrown

set_countries.discard('arg')        # ← '.discard' handles the exception when the element is typed wrongly
print(set_countries)        # {'pe', 'br', 'ecua', 'col', 'mx', 'uru', 'ar', 'ven'}

set_countries.remove('ar')
print(set_countries)        # {'col', 'ven', 'ecua', 'pe', 'br', 'uru', 'mx'}

set_countries.add('arg')        # ← correct name
print(set_countries)        # {'br', 'col', 'uru', 'pe', 'ven', 'mx', 'ecua', 'arg'}

# -----------------------------

# clearing the set completely

set_countries.clear()       
print(set_countries)    # set()
print(len(set_countries))   # 0
