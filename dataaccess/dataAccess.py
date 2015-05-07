from google.appengine.ext import ndb
import webapp2

class Usuario(ndb.Model):
    name = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)
    password = ndb.StringProperty(indexed=True)

class SeeUsers():
    usuarios = ndb.gql("SELECT * FROM Usuario")

class AddUsers(webapp2.RequestHandler):
    def get(self):
        usuario = Usuario()
        usuario.name="lau"
        usuario.email="lau001@gmail.com"
        usuario.password="lau001"
        usuario.put()