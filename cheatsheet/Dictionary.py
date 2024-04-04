# In Java map
empty = {}
print(empty)

food = {"Salad": "yes", "Steak": "no", "Cake": "yes"}
print(food)

food["Steak"] = "yes"
print(food)

# Dictionary länge
print(len(food))    # output 3

# Verschachteltes Dictionary
deEn = {"rot": "red", "blau": "blue", "grün": "green"}
enFr = {"red": "rouge", "blue": "bleu", "green": "vert"}

print(deEn["rot"])
print(enFr[deEn["rot"]])

# Dictionary von Dictionaries
enDe = {"red": "rot", "blue": "blau", "green": "grün"}
deFr = {"rot": "rouge", "blau": "bleu", "grün": "vert"}

dictionaries = {"enDe": enDe, "deFr": deFr}
print(dictionaries["deFr"]["blau"])

# Dictionary verändern
capitals = {"Schweiz": "Bern", "Östereich": "Wien"}
capital = capitals.pop("Östereich")
print(capital)
print(capitals)

capital = capitals.pop("Deutschland", "Unbekannt")
print(capital)

capital = capitals.get("Schweiz")
print(capital)  # Gibt Bern aus

# Dictionary in Liste/Set umwandel
dD = {"Eins", "Zwei"}
print(dD)

dL = list(dD)
print(dL)

dS = set(dD)
print(dS)

"""
len(d)      Liefert Anzahl Elemente im Dictionary
clear(d)    leert das Dictionary ohne es zu löschen
update(d)   Ein weiteres Dictionary einhängen
keys()      Liefert die Schlüssel zurück
values()    Liefert die Werte zurück
del d[k]    Löst den Schlüssel k mit seinem Wert
k in d      True wenn in Dictionary d Schlüssel k ist
k not in d  True wenn in Dictionary d kein Schlüssel k ist
"""
