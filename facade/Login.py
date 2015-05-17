import webapp2

from dataaccess import dataAccess
from interface import LoginInterface
from interface import Start
import config


class Login(webapp2.RequestHandler):
    def write_form(self, username="", password=""):
        self.response.out.write(config.htmlFirst())
        self.response.out.write(Start.menu() + LoginInterface.loginhtml() % {"username": username, "password": password})
        self.response.out.write(config.htmlEnd())
    def get(self):
        self.write_form()
    def post(self):
        email = self.request.get("email")
        passw = self.request.get("password")
        dbEmail = dataAccess.Usuario.email
        dbPass = dataAccess.Usuario.password
        usuario = dataAccess.Usuario.query(dbEmail == email, dbPass == passw)
        if usuario.count() == 1:
            self.redirect("/app?username=%s" % email)
        else:
            self.response.write("Wrong user. <a href=\"/\">return</a>")

app = webapp2.WSGIApplication([
    ('/login', Login)
], debug=True)\
