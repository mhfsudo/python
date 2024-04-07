# Tuple können im Gegensatz zu Listen nicht veränder werden
t = ("Basel", "Bern", "Zürich")
print(t)
print(t[1])

# Tuple constructor
t = tuple(("Basel", "Bern", "Zürich"))
print(t)

# Tuple länge
print(len(t))   # output 3

# Tuple workaround for change an item
t2 = list(t)
t2.append("Aarau")
l = tuple(t2)
print(l)    # output ('Basel', 'Bern', 'Zürich', 'Aarau')

# loop tuple
for x in l:
    print(x)
