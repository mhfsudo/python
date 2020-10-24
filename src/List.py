#Liste
staedte = ["Basel", "Bern", "Zuerich"]
print(staedte)

#Liste kuerzen
print(staedte[1:3])

#Liste umkehren
print(staedte[::-1])

#Listeninhalt kontrollieren
print("Bern" in staedte)
print("Luzern" in staedte)

#Listenelement hinzufügen
staedte = ["Basel", "Bern", "Zuerich"]
staedte.append("Luzern")
print(staedte)

staedtePlus = ["Neuenburg", "Zug"]
staedte.extend(staedtePlus)
print(staedte)

staedte.insert(0, "Aarau")
print(staedte)

#Listenelement entfernen
staedte.pop(3)
print(staedte)

staedte.remove("Neuenburg")
print(staedte)

#Liste kopieren
list1 = ['a','b']
list2 = list1

print(list1)
print(list2)

#Verschachtelte Liste kopieren
from copy import deepcopy

list1 = ['a','b',['ab','ba']]
list2 = deepcopy(list1)

print(list1)
print(list2)

"""
[]                    leere Liste
[1,2,3]               Liste mit Ganzzahlen
[1,"Eins",1.1]        Liste mit gemischten Datentypen
["Eins","Zwei"]       Liste mit Strings
[["Bern", 133000]]    Verschachtelte Liste
["1",["2"["3"]]]      tief verschachtelte Liste
"""