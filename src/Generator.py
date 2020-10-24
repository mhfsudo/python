def abc_generator():
    yield("a")
    yield("b")
    yield("c")

gen1 = abc_generator()
gen2 = abc_generator()

letter = next(gen1)
print(letter)

letter = next(gen1)
print(letter)

letter = next(gen2)
print(letter)

letter = next(gen2)
print(letter)

#https://www.python-kurs.eu/python3_generatoren.php