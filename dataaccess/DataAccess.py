from google.appengine.ext import ndb
import config


class Usuario(ndb.Model):
    name = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)
    password = ndb.StringProperty(indexed=True)
    admin = ndb.BooleanProperty

def SeeUsers(self):
    usuarios = Usuario.query()
    self.response.out.write('<table>')
    for usuario in usuarios:
        self.response.out.write('<tr>')
        self.response.out.write('<td>' + usuario.email + '</td>')
        self.response.out.write('<td>' + usuario.name + '</td>')
        self.response.out.write('</tr>')
    self.response.out.write('</table>' + config.htmlEnd())


def AddUsers():
    usuario2 = Usuario()
    usuario2.name = "andoni"
    usuario2.email = "andoni@gmail.com"
    usuario2.password = "andoni"
    usuario2.admin = False
    usuario2.put()

    usuario = Usuario()
    usuario.name = "laura"
    usuario.email = "laura@gmail.com"
    usuario.password = "laura"
    usuario.admin = True
    usuario.put()

    admin = Usuario()
    admin.name = "admin"
    admin.email = "admin"
    admin.password = "admin123"
    admin.put()

class Elemento(ndb.Model):
    idElement = ndb.StringProperty(required=True)
    name = ndb.StringProperty(required=True)
    price = ndb.StringProperty(required=True)
    photo = ndb.StringProperty(required=True)
    type = ndb.StringProperty(required=True)

def AddElements(self):
    for i in xrange(1, 11):
        e1 = Elemento()
        e1.idElement = "" + i.__str__() + ""
        e1.name = "Name" + i.__str__()
        e1.photo = "/images/img" + i.__str__() +".png"
        if i % 3 == 0:
            e1.type = "food"
            e1.price = "20"
        elif i % 2 == 0:
            e1.type = "drink"
            e1.price = "3"
        else:
            e1.type = "dessert"
            e1.price = "5"
        e1.put()
        self.response.out.write(e1.idElement + " ")

def getElements(type):
    return Elemento.query(Elemento.type == type)

def getLastElementId():
    return Elemento.query(Elemento).count + 1




#usuarios = ndb.gql("SELECT * FROM Usuario")
