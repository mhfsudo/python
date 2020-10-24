def Hello(name="everybody"):
    """Greets a person (This is the Docstring)"""
    print("Hello " + name + "!")

print("The docstring of the function Hello: " + Hello.__doc__)