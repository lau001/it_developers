import webapp2

import re
import cgi
from interface import signupInterface
from dataaccess import dataAccess
import App
import config



#Global
USER_RE = re.compile("^[a-zA-Z0-9_-]{3,20}$")
PASSWORD_RE = re.compile("^.{3,20}$")
EMAIL_RE = re.compile("^[\S]+@[\S]+\.[\S]+$")

class Signup(webapp2.RequestHandler):
    def write_form(self, username="", password="", verify="", email="", username_error="", password_error="", verify_error="", email_error=""):
        self.response.out.write(config.htmlFirst())
        self.response.out.write(signupInterface.signup_form() % {"username": username, "password": password,
            "verify":verify, "email": email, "username_error": username_error, "password_error": password_error, "verify_error": verify_error, "email_error": email_error})
        self.response.out.write(config.htmlEnd())
    def get(self):
        self.write_form()
    def post(self):
        user_username = self.request.get("username")
        user_password = self.request.get("password")
        user_verify= self.request.get("verify")
        user_email = self.request.get("email")
        sani_username = self.escape_html(user_username)
        sani_password = self.escape_html(user_password)
        sani_verify= self.escape_html(user_verify)
        sani_email = self.escape_html(user_email)
        username_error = ""
        password_error = ""
        verify_error = ""
        email_error = ""
        error = False
        if not self.valid_username(user_username):
            username_error = "Invalid username. "
            error = True
        if not self.valid_password(user_password):
            password_error = "Invalid password. "
            error = True
        if not user_verify or not user_password == user_verify:
            verify_error = "Passwords do not match"
            error = True
        if not self.valid_email(user_email):
            email_error = "Invalid email"
            error = True

        if error:
            self.write_form(sani_username, sani_password, sani_verify, sani_email, username_error, password_error, verify_error, email_error)
        else:
            user = dataAccess.Usuario.query(dataAccess.Usuario.name == user_username)

            if user.count() == 0:
                u = dataAccess.Usuario()
                u.name = user_username
                u.email = user_email
                u.password = user_password
                u.put()

                self.redirect("/app?username=%s" % user_username)
            else:
                self.write_form(sani_username, sani_password, sani_verify, sani_email, username_error, password_error, verify_error, email_error)
                self.response.out.write("User already exists")

    def valid_username(self, username):
        return USER_RE.match(username)
    def valid_password(self, password):
        return PASSWORD_RE.match(password)
    def valid_email(self, email):
        return EMAIL_RE.match(email)

    def escape_html(self, val):
        return cgi.escape(val, quote=True)

app = webapp2.WSGIApplication([
    ('/signup', Signup), ('/app', App.App)
], debug=True)