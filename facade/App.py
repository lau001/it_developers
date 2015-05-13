import webapp2
from interface import start
import config

class App(webapp2.RequestHandler):
    def get(self):
        self.response.write(config.htmlFirst() + start.loggedMenu() + config.htmlEnd())

app = webapp2.WSGIApplication([
    ('/app', App)
], debug=True)