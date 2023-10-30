#List comprehension
z = ["alpha", "bravo", "charlie"]
new_z = [i[0]*2 for i in z]
print(new_z)

# WHAT IT DOES
# The list comprehension iterates through each element i in the list z.
# For each element i, it takes the first character (i.e., i[0]) and doubles it (*2).
# The result of that operation is appended to the new list new_z.

#output: ['aa', 'bb', 'cc']