import webapp2

from interface import index


class App(webapp2.RequestHandler):
    def get(self):
        self.response.write(index.startapp)

app = webapp2.WSGIApplication([
    ('/app', App)
], debug=True)