import webapp2

from dataaccess import dataAccess
from interface import login
import App


class Login(webapp2.RequestHandler):
    def write_form(self, username="", password=""):
        self.response.out.write(login.loginhtml % {"username": username, "password": password})
    def get(self):
        self.write_form()
    def post(self):
        email = self.request.get("email")
        passw = self.request.get("password")
        dbEmail = dataAccess.Usuario.email
        dbPass = dataAccess.Usuario.password

        user = dataAccess.Usuario.query(dbEmail == email, dbPass == passw)
        if user.count() == 1:
            self.redirect("/app?username=%s" % email)
        else:
            self.response.write(email % ", " % dbEmail % " Wrong user. <a href=\"/\">return</a>")

app = webapp2.WSGIApplication([
    ('/login', Login), ('/app', App.App)
], debug=True)