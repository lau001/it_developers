#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import cgi
import re

import webapp2
from google.appengine.api import users
from google.appengine.ext import ndb

from interface import login, signup, start


class Usuario(ndb.Model):
    name = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)
    password = ndb.StringProperty(indexed=True)

class Main(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()


        if user:
            msg = ("Welcome, %s! (<a href=\"%s\">logout</a></br><a href=\"/app\"> app </a>)"%
                   (user.nickname(), users.create_logout_url("/")))
        else:
            msg = ("<form action=\"/loginform\">"
                   "<input type=\"submit\" value=\"Login\">"
                   "</form>")
        self.response.out.write("<html><body>%s</body></html>" % msg)

USER_RE = re.compile("^[a-zA-Z0-9_-]{3,20}$")
PASSWORD_RE = re.compile("^.{3,20}$")
EMAIL_RE = re.compile("^[\S]+@[\S]+\.[\S]+$")

class SignupHandler(webapp2.RequestHandler):
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
            user = Usuario.query(Usuario.name==user_username,Usuario.email==user_email).count()
            if user==0:
                u=Usuario()
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




class App(webapp2.RequestHandler):
    def get(self):
        self.response.write(start.startapp)

class LoginForm(webapp2.RequestHandler):
    def get(self):
        self.response.write(login.loginhtml)

class Login(webapp2.RequestHandler):
    def get(self):
        email= self.request.get("email")
        passw = self.request.get("password")

        user = users.User(email)
        usuario = Usuario(email,passw)

        if email=="text.example@gmail.com":
            self.redirect('/app')
        else:
            self.response.write("Wrong password. Try again: <a href=\"/loginform\">logout</a> " )

class Logout(webapp2.RequestHandler):
    def get(self):
        users.create_logout_url('/')
        self.redirect('/')

class AddUsers(webapp2.RequestHandler):
    def get(self):
        usuario = Usuario()
        usuario.name="lau"
        usuario.email="lau001@gmail.com"
        usuario.password="lau001"
        usuario.put()

class SeeUsers(webapp2.RequestHandler):
    def get(self):
        usuarios = ndb.gql("SELECT * FROM Usuario")
        self.response.out.write('<table border = 1>')
        for usuario in usuarios:
            self.response.out.write('<tr>')
            self.response.out.write('<td>'+usuario.email+'</td>')
            self.response.out.write('<td>'+usuario.name+'</td>')
            self.response.out.write('</tr>')
            self.response.out.write('</table>')

app = webapp2.WSGIApplication([
    ('/', Main), ('/app', App), ('/loginform', SignupHandler), ('/login', Login), ('/logout', Logout), ('/users',SeeUsers), ('/addusers',AddUsers)
], debug=True)
