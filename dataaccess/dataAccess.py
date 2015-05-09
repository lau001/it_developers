from google.appengine.ext import ndb
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

def AddUsers(self):
    usuario = Usuario()
    usuario.name = "lau"
    usuario.email = "lau001@gmail.com"
    usuario.password = "lau001"
    usuario.put()

#usuarios = ndb.gql("SELECT * FROM Usuario")