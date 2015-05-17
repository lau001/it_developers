import webapp2
from interface import Start
import config

class App(webapp2.RequestHandler):
    def get(self):
        self.response.write(config.htmlFirst() + Start.menu() + config.htmlEnd())

app = webapp2.WSGIApplication([
    ('/app', App)
], debug=True)