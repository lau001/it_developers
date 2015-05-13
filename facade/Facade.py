import webapp2
from google.appengine.api import users

from dataaccess import DataAccess

#LOGOUT

class Logout(webapp2.RequestHandler):
    def get(self):
        users.create_logout_url('/')
        self.redirect('/')


#SEE DATABASE USER

class SeeUsers(webapp2.RequestHandler):
    def get(self):
        return DataAccess.SeeUsers(self)

class AddUsers(webapp2.RequestHandler):
    def get(self):
        return DataAccess.AddUsers()