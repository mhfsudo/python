#Das * vor der Variable bedeutet variable Anzahl von Parametern
def arithmetic_mean(*args):
    sum = 0
    for x in args:
        sum += x
    return sum

print(arithmetic_mean(45, 32, 89, 78))
print(arithmetic_mean(8989.8, 78787.78, 3453, 78778.73))
print(arithmetic_mean(45, 32))
print(arithmetic_mean(45))
print(arithmetic_mean())

#Das ** vor der Variable bedeutet variable Anzahl von Schlüsselwortparametern
def f(a,b,x,y):
    print(a, b, x, y)

d = {'a':'append':"1", 'b':'block':"2", 'x':'extract':"3", 'y':'yes':"4"}
f(*d)       #Ausgabe a b x y
f(**d)      #Azsgabe apped block extraxt yes

#Es können auch Pflichtparameter festgelegt werden
#vorname = Pflicht nachname = optional
def name(vorname, *nachname):
    print(vorname, nachname)

name("Michael")
name("Michael", "Friderich")

