"""Show the identity of a instance"""
x = 42
print(id(x))

y = x
print(id(x), id(y))

y = 78
print(id(x), id(y))