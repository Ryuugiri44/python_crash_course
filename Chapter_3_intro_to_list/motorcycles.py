motorcycles = ['honda','yamaha','suzuki']

print(motorcycles)

# motorcycles[0] = 'ducati'
# print(motorcycles)

# Adding a new variable in the list, but it will be located at the end

motorcycles.append('ducati')
print(motorcycles)

# Inserting a new variable
motorcycles = ['honda','yamaha','suzuki']
motorcycles.insert(0,'ducati')
print(motorcycles)

# Removing a variable
del motorcycles[0]
print(motorcycles)

# Removing an item using pop() Method
motorcycles = ['honda','yamaha','suzuki']
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

# You can also remove any element with pop
motorcycles = ['honda','yamaha','suzuki']
popped_motorcycles = motorcycles.pop(0)
print(motorcycles)

# When we don't know the location of the element we want to remove
## we can use the remove method

motorcycles = ['honda','yamaha','suzuki']

motorcycles.remove('yamaha')
print(motorcycles)

# We can even assign the value to a variable and use it in the remove method

motorcycles = ['honda','yamaha','suzuki','ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(f"A {too_expensive} is too expensive for me.")