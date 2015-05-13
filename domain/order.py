class Order:

    def __init__(self, idOrder, email, listElement, date, totalPrice):
        self.__idOrder = idOrder
        self.__email = email
        self.__listElement = listElement
        self.__date = date
        self.__totalPrice = totalPrice

    def getIdElement(self):
        return self.__idOrder

    def getEmail(self):
        return self.__email

    def getListElement(self):
        return self.__listElement

    def getDate(self):
        return self.__date

    def getTotalPrice(self):
        return self.__listElement

    def setIdOrder(self, idOrder):
        self.__idOrder = idOrder

    def setEmail(self, email):
        self.__email = email

    def setListElement(self, listElement):
        self.__listElement = listElement

    def setDate(self, date):
        self.__date = date

    def setPhoto(self, totalPrice):
        self.__totalPrice = totalPrice

def make_order(idOrder, email, listElement, date, totalPrice):
    order = Order(idOrder, email, listElement, date, totalPrice)
    return order