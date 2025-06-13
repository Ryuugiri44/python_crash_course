# We will look at sorting the variables alphabetically 

cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)

# The sort method will change the order of the list permanently 
# If we want the opposite, we include reverse = True

cars.sort(reverse=True)
print(cars)

# If we only want a temporary sort, then we use the sorted() function
cars = ['bmw','audi','toyota','subaru']
print("This is the original")
print(cars)

print("\n This is with the sorted function")
print(sorted(cars))
print("\nThis is the original")
print(cars)

# reverse method
# This will simply reverse the order, but not alphabetically
cars.reverse()
print(cars)

# This is to find the length of a list
print(len(cars))


# Indexing
print(cars[0])
# Indexing backwards
print(cars[-1])