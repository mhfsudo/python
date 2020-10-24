#Division durch Null
x = 10
for y in [3, 0, 1]:
    try:
        z = x / y
    except:
        z = None
    print("z: ", z)

#Eingabekontrolle
while True:
    try:
        n = input("Bitte eine Ganzzahl (integer) eingeben: ")
        n = int(n)
        break
    except ValueError:
        print("Keine Integer! Bitte nochmals versuchen ...")
    #else: optional
    finally:
        print("Finally wird immmer ausgeführt")
print("Super! Das war's!")