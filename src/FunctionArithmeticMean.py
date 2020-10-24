#Das Arithmetische Mittel wird berechnet
#Der Pflichtparameter x dient dazu das sicher 2 Zahlen übergeben werden müssen
#Damit wird Division durch 0 verhindert
def arithmeticMean(x, *numbers):
    sum = x
    for i in numbers:
        sum += i
    return sum / (1.0 + len(numbers))

print(arithmeticMean(4,5))
print(arithmeticMean(4,7,9))

#Wenn die Funktion mit einer Liste aufgerufgen werden möchte,
#muss ein * verwendet werden
l1 = [4,5]
print(arithmeticMean(*l1))
l2 = [4,7,9]
print(arithmeticMean(*l2))

def f(x,y,z):
    print(x,y,z)

#Funktionsaufruf mit *
p = (1,2,3)
#Gut
f(*p)
#Schlecht
f(p[0],p[1],p[2])