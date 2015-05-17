from google.appengine.ext import ndb
from domain import Element
import config


class Usuario(ndb.Model):
    name = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)
    password = ndb.StringProperty(indexed=True)

def SeeUsers(self):
    usuarios = Usuario.query()
    self.response.out.write(config.htmlFirst() + '<table border = 1>')
    for usuario in usuarios:
        self.response.out.write('<tr>')
        self.response.out.write('<td>' + usuario.email + '</td>')
        self.response.out.write('<td>' + usuario.name + '</td>')
        self.response.out.write('</tr>')
    self.response.out.write('</table>' + config.htmlEnd())

def AddUsers():
    usuario2 = Usuario()
    usuario2.name = "andoni"
    usuario2.email = "andoniito@gmail.com"
    usuario2.password = "andoni"
    usuario2.put()

    usuario = Usuario()
    usuario.name = "carla"
    usuario.email = "carla@gmail.com"
    usuario.password = "carla"
    usuario.put()


def getElementId():
    return 1


#usuarios = ndb.gql("SELECT * FROM Usuario")
