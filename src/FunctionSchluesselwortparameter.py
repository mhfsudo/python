def sumsub(a, b, c=0, d=0):
    "c und d haben einen default wert der nicht angegeben werden muss, aber kann"
    return a - b + c - d

print(sumsub(12,4))
print(sumsub(42,15,d=10))