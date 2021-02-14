cars = ["Ford", "Volvo", "BMW"]

print(cars[0])  # output Ford

# Array länge
print(len(cars)) # output 3

# Adding element
cars.append("Skoda")

# Remove element
cars.pop(0)
cars.remove("BMW")

# loop array
for x in cars:
    print(x)