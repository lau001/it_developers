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
        </body>

    </html>

"""

class Main(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()


        if user:
            msg = ("Welcome, %s! (<a href=\"%s\">sign out</a></br><a href=\"/app\"> app </a>)"%
                   (user.nickname(), users.create_logout_url("/")))
        else:
            msg = ("<form action=\"%s\">"
                   "<input type=\"submit\" value=\"Login\">"
                   "</form>" %
                   users.create_login_url("/"))
        self.response.out.write("<html><body>%s</body></html>" % msg)



class App(webapp2.RequestHandler):
    def get(self):
        self.response.write(startapp)

app = webapp2.WSGIApplication([
    ('/', Main), ('/app', App)
], debug=True)
