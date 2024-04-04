# Set Elemente haben keinen festen Platz
s = {"Basel", "Bern", "Zürich"}
print(s)

# Set constructor
s = set(("Basel", "Bern", "Zürich"))

# Set länge
print(len(s))   # output 3

# Set prüfen
print("Bern" in s)  # output True
print("Aarau" in s) # output False

s = {("Basel", 172000), ("Bern", 133000), ("Zürich", 514000)}
print(s)

#Set erweitern
s = {"Basel", "Bern", "Zürich"}
s.add("Zug")

#Es können keine Elemente doppelt vorkommen
s.add("Bern")
print(s)

# loop set
for x in s:
    print(x)