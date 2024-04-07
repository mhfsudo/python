#For
#Else wird nur ausgeführt weine keine break Anweisung vorhanden ist
languages = ["C#", "Java", "Kotlin"]

for language in languages:
    print(language)
else:
    print("I don't know more languages")

#Break
edibles = ["Salad", "Steak", "Cake"]

for food in edibles:
    if food == "Steak":
        print("No more Steak please!")
        break
    print("Great, delicious " + food)
else:
    print("I am so glad: No Steak!")

print("Finally, I finished stuffing myself")

#Continue
edibles = ["Salad", "Steak", "Cake"]

for food in edibles:
    if food == "Steak":
        print("No more Steak please!")
        continue
    print("Great, delicious " + food)
else:
    print("I am so glad: No Steak!")

print("Finally, I finished stuffing myself!")