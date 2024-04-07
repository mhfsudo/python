"""
name    Public      in und auserhalb Klasse
_name   Protected   in und auserhalb Klasse, Member sollte aber nicht benutzt werden
__name  Private     nur innerhalt Klasse
"""

class A():

    def __init__(self):
        self.__priv = "Privat"
        self._prot  = "Protected"
        self.pub    = "Public"

x = A()

print(x.pub)
x.pub = "Wert kann verändert werden"
print(x.pub)

print(x._prot)
x._prot = "Wert kann verändet werden, sollte aber nicht"
print(x._prot)

print(x.__priv)
#Erzeugt eine Fehlermeldung