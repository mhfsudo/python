class Roboter:

    #Initalisierung der Atributte
    def __init__(self, name, age):
        print("__init__ wurde ausgeführt!")
        self.__name = name
        self.__age = age

    def sayHello(self):
        print("Hallo " + self.__name)

    #setter
    def setName(self, name):
        self.__name = name
    #getter
    def getName(self):
        return self.__name

    def setAge(self, age):
        self.__age = age

    def getAge(self):
        return str(self.__age)

if __name__ == "__main__":
    x = Roboter("Michael", 29)
    x.sayHello()
    print("Alter: " + x.getAge())
    x.setAge(30)
    print("Alter: " + x.getAge())

    y = Roboter("Lisa", 29)
    y.sayHello()
