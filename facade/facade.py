import webapp2

from dataaccess import dataAccess
from google.appengine.api import users

#LOGOUT

class Logout(webapp2.RequestHandler):
    def get(self):
        users.create_logout_url('/')
        self.redirect('/')


#SEE DATABASE USER

class SeeUsers(webapp2.RequestHandler):
    def get(self):
        return dataAccess.SeeUsers(self)

def AddUsers():
    return dataAccess.AddUsers