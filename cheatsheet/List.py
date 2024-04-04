# Liste
l = ["Basel", "Bern", "Zuerich"]
print(l)

# List constructor
l = list(("Basel", "Bern", "Zürich"))

# Liste kuerzen
print(l[1:3]) # output ['Bern', 'Zuerich']

# Liste umkehren
print(l[::-1]) # output ['Zuerich', 'Bern', 'Basel']

# Listeninhalt kontrollieren
print("Bern" in l)    # output True
print("Luzern" in l)  # output False

# Listenelement hinzufügen
l = ["Basel", "Bern", "Zuerich"]
l.append("Luzern")
print(l)

staedtePlus = ["Neuenburg", "Zug"]
l.extend(staedtePlus)
print(l)

l.insert(0, "Aarau")
print(l)

# Listenelement entfernen
l.pop(3)
print(l)

l.remove("Neuenburg")
print(l)

# Liste kopieren
list1 = ['a', 'b']
list2 = list1
print(list1)    # output ['a', 'b']
print(list2)    # output ['a', 'b']

# Liste länge
print(len(list1))   # output 2

# Verschachtelte Liste kopieren
from copy import deepcopy
list1 = ['a', 'b', ['ab', 'ba']]
list2 = deepcopy(list1)
print(list1)
print(list2)

# loop list
for x in l:
    print(x)

"""
[]                    leere Liste
[1,2,3]               Liste mit Ganzzahlen
[1,"Eins",1.1]        Liste mit gemischten Datentypen
["Eins","Zwei"]       Liste mit Strings
[["Bern", 133000]]    Verschachtelte Liste
["1",["2"["3"]]]      tief verschachtelte Liste
"""
