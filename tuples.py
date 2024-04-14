# Creating a tuple
cars = ("Jeep", "Benz", "Toyota", "Nissan", "Subaru")
print(cars)
print(cars[1:-2])
print(len(cars))

# Accessing an item
cars = ("Jeep", "Benz", "Toyota", "Nissan", "Subaru")
print(cars[4])


# Adding an item , you change first into a list
cars2 = list(cars)
print(cars2)
cars2.append("Prado")
print(cars2)

cars2.extend(["Probox", "Range"])
print(cars2)
print(cars2.pop())

# Printing each item
for x in cars2: 
 print(x)

cars = tuple(cars2)
print

