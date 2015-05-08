import webapp2
from google.appengine.api import users

from dataaccess import dataAccess


class Logout(webapp2.RequestHandler):
    def get(self):
        users.create_logout_url('/')
        self.redirect('/')


#SEE DATABASE USERS

class SeeUsers(webapp2.RequestHandler):
    def get(self):
        return dataAccess.SeeUsers(self)


#ADD USERS TO DATABASE

class AddUsers():
    def get(self):
        return dataAccess.AddUsers(self)

