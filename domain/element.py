class Element:

    def __init__(self, idElement, name, price, photo, type):
        self.__idElement = idElement
        self.__name = name
        self.__price = price
        self.__photo = photo
        self.__type = type

    def getIdElement(self):
        return self.__idElement

    def getName(self):
        return self.__name

    def getPrice(self):
        return self.__price

    def getPhoto(self):
        return self.__photo

    def getType(self):
        return self.__type

    def setIdElement(self, idElement):
        self.__idElement = idElement

    def setName(self, name):
        self.__name = name

    def setPrice(self, price):
        self.__price = price

    def setPhoto(self, photo):
        self.__photo = photo

    def setType(self, type):
        self.__type = type

def make_element(idElement, name, price, photo, type):
    element = Element(idElement, name, price, photo, type)
    return element