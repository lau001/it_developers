import webapp2
from interface import appInterface

class App(webapp2.RequestHandler):
    def get(self):
        self.response.write(appInterface.add_element_gui())

app = webapp2.WSGIApplication([
    ('/app', App)
], debug=True)