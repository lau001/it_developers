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
import webapp2
from google.appengine.api import users
from google.appengine.ext import db



startapp = """\

  <!doctype html>
    <html>
        <body>
            <div> Hello there! </div>
            <form>
                <div> <a href=\"/logout\">logout</a></br> </div>
            </form>
        </body>

    </html>

"""

loginhtml = """\

  <!doctype html>
    <html>
        <body>

            <form action=\"/login\">
                <div> Email: <input type=\"text\" name=\"email\"/> </div>
                <div> Password: <input type=\"password\" name=\"password\"/> </div>
                <div> <input type=\"submit\" value=\"Login\"</div>
            </form>
        </body>

    </html>

"""


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



class App(webapp2.RequestHandler):
    def get(self):
        self.response.write(startapp)

class LoginForm(webapp2.RequestHandler):
    def get(self):
        self.response.write(loginhtml)

class Login(webapp2.RequestHandler):
    def get(self):

        self.redirect('/app')

class Logout(webapp2.RequestHandler):
    def get(self):
        users.create_logout_url('/')
        self.redirect('/')

app = webapp2.WSGIApplication([
    ('/', Main), ('/app', App), ('/loginform', LoginForm), ('/login', Login), ('/logout', Logout)
], debug=True)
