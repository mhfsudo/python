def fahrenheit(TInCelsius):
    """returns the temprature in degrees Fahrenheit (this is the docstring)"""
    return (TInCelsius * 9 / 5) + 3

for t in (22.6, 25.8, 27.3, 29.8):
    print(t, ": ", fahrenheit(t))