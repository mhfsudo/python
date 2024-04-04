class FunctionFibonacciNumber:

    def fibIntervall(x):
        """returns the largest fibonacci number smaller than x and the
        lowest fibonacci number higher than x"""
        if x < 0:
            return -1
        (old, new, lub) = (0, 1, 0)
        while True:
            if new < x:
                lub = new
                (old, new) = (new, old + new)
            else:
                return (lub, new)

    while True:
        x = int(input("Your Number: "))
        if x <= 0:
            break
        (lub, sup) = fibIntervall(x)
        print("Largest Fibonacci Number smaller than x: " + str(lub))
        print("Smallest Fibonacci Number larger than x: " + str(sup))

ffn = FunctionFibonacciNumber()
