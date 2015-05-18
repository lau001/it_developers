import webapp2

from dataaccess import DataAccess

#LOGOUT

class Logout(webapp2.RequestHandler):
    def get(self):
        self.response.headers.add_header('Set-Cookie',"logged=false")
        self.response.headers.add_header('Set-Cookie',"username=")
        self.redirect('/')


#SEE DATABASE USER

class SeeUsers(webapp2.RequestHandler):
    def get(self):
        return DataAccess.SeeUsers(self)

class AddUsers(webapp2.RequestHandler):
    def get(self):
        return DataAccess.AddUsers()

class AddElements(webapp2.RequestHandler):
    def get(self):
        return DataAccess.AddElements(self)
