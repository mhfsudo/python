#In Java Lambda-Operator, Funktionen map, filter, reduce
Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = [((float(9)/5)*x + 32) for x in Celsius]
print(Fahrenheit)

#Set Comprehension
from math import sqrt
n = 100
sqrt_n = int(sqrt(n))
no_primes = {j for i in range(2, sqrt_n -1) for j in range(i*2, n, i)}
print(no_primes)
primes = {i for i in range(n) if i not in no_primes}
print(primes)

#Generator Comprehension
x = (x **2 for x in range(20))
print(x)
x = list(x)
print(x)

#See also PrimesTest