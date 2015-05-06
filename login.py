import webapp2
from google.appengine.api import users




class LoginHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', LoginHandler)
], debug=True)