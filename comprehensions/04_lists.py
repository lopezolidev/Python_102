# "traditional" approach

numbers = []

for element in range(1, 11):
    numbers.append(element)

print("numbers: ",numbers)      # numbers:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# list-comprehension 

numbers_v2 = [element for element in range(1, 11)]

print("numbers_v2: ",numbers_v2)        # numbers_v2:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# now with conditions

numbers_v3 = []

for i in range(1, 11):
    if i % 2 == 0:
        numbers_v3.append(i * 2)

print("numbers_v3: ", numbers_v3)       # numbers_v3:  [4, 8, 12, 16, 20]

numbers_v4 = [i * 2 for i in range(1, 11) if i % 2 == 0]
print("numbers_v4", numbers_v4)     # numbers_v4 [4, 8, 12, 16, 20]


# Now with another condition

numbers_v5 = [i / 3 for i in range(1, 101) if i % 3 == 0]
print("numbers_v5: ",numbers_v5)       # numbers_v5: [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0, 25.0, 26.0, 27.0, 28.0, 29.0, 30.0, 31.0, 32.0, 33.0]



