import webapp2
from google.appengine.api import users

from dataaccess import dataAccess

#LOGOUT

class Logout(webapp2.RequestHandler):
    def get(self):
        self.response.headers.add_header('Set-Cookie',"logged=false")
        self.response.headers.add_header('Set-Cookie',"username=")
        self.redirect('/')


#SEE DATABASE USER

class SeeUsers(webapp2.RequestHandler):
    def get(self):
        return dataAccess.SeeUsers(self)

class AddUsers(webapp2.RequestHandler):
    def get(self):
        return dataAccess.AddUsers()

class AddElements(webapp2.RequestHandler):
    def get(self):
        return dataAccess.AddElements(self)
