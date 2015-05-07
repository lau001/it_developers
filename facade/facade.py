import webapp2
import re
import cgi
from interface import login, signup, start
from dataaccess import dataAccess
from google.appengine.api import users

#Global
USER_RE = re.compile("^[a-zA-Z0-9_-]{3,20}$")
PASSWORD_RE = re.compile("^.{3,20}$")
EMAIL_RE = re.compile("^[\S]+@[\S]+\.[\S]+$")

#INTERFACES

class App(webapp2.RequestHandler):
    def get(self):
        self.response.write(start.startapp)

class LoginForm(webapp2.RequestHandler):
    def get(self):
        self.response.write(login.loginhtml)


#SIGIN

class Signup(webapp2.RequestHandler):
    def write_form (self, username="", password="",verify="", email="", username_error="", password_error="",verify_error="",email_error=""):
        self.response.out.write(signup.signup_form % {"username" : username, "password" : password,
            "verify" : verify, "email" : email, "username_error" : username_error, "password_error" : password_error,"verify_error" : verify_error, "email_error" : email_error})
    def get(self):
        self.write_form()
    def post(self):
        user_username = self.request.get('username')
        user_password = self.request.get('password')
        user_verify= self.request.get('verify')
        user_email = self.request.get('email')
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
            username_error = "Wrong name."
            error = True
        if not self.valid_password(user_password):
            password_error = "Wrong password. "
            error = True
        if not user_verify or user_password == user_verify:
            verify_error = "Passwords do not match"
            error = True
        if not self.valid_email(user_email):
            email_error = "Wrong email"
            error = True

        if error:
            self.write_form(sani_username,sani_password,sani_verify,sani_email,username_error,password_error,verify_error,email_error)
        else:
            user = dataAccess.Usuario.query(dataAccess.Usuario.name==user_username,dataAccess.Usuario.email==user_email).count()
            if user==0:
                u=dataAccess.Usuario()
                u.name=user_username
                u.email=user_email
                u.password=user_password
                u.put()
                self.redirect("/app?username=%s" % user_username)
            else:
                self.write_form(sani_username,sani_password,sani_verify,sani_email,username_error,password_error,verify_error,email_error)
                self.response.out.write("User already exists")

    def valid_username(self,username):
        return USER_RE.match(username)
    def valid_password(self,password):
        return PASSWORD_RE.match(password)
    def valid_email(self,email):
        return EMAIL_RE.match(email)

    def escape_html(self,val):
        return cgi.escape(val, quote=True)


#LOGIN

class Login(webapp2.RequestHandler):
    def get(self):
        email= self.request.get("email")
        passw = self.request.get("password")

        user = users.User(email)
        usuario = dataAccess.Usuario(email,passw)

        if email=="text.example@gmail.com":
            self.redirect('/app')
        else:
            self.response.write("Wrong password. Try again: <a href=\"/loginform\">logout</a> " )

#LOGOUT

class Logout(webapp2.RequestHandler):
    def get(self):
        users.create_logout_url('/')
        self.redirect('/')


#SEE DATABASE USERS

class SeeUsers(webapp2.RequestHandler):
    def get(self):
        #usuarios = ndb.gql("SELECT * FROM Usuario")
        usuarios = dataAccess.SeeUsers.usuarios
        self.response.out.write('<table border = 1>')
        for usuario in usuarios:
            self.response.out.write('<tr>')
            self.response.out.write('<td>'+usuario.email+'</td>')
            self.response.out.write('<td>'+usuario.name+'</td>')
            self.response.out.write('</tr>')
        self.response.out.write('</table>')

def AddUsers():
    return dataAccess.AddUsers