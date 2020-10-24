#Menge (Elemente haben keinen festen Platz
stadte = {"Basel", "Bern", "Zürich"}
print(stadte)

print("Bern" in stadte)
print("Aarau" in stadte)

stadte = {("Basel", 172000), ("Bern", 133000), ("Zürich", 514000)}
print(stadte)

#Set erweitern
stadte = {"Basel", "Bern", "Zürich"}
stadte.add("Zug")
#Es können keine Elemente doppelt vorkommen
stadte.add("Bern")
print(stadte)