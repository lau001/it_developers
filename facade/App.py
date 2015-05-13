import webapp2

class App(webapp2.RequestHandler):
    def get(self):

        self.response.write("ANDONI PAGAFANTER")


app = webapp2.WSGIApplication([
    ('/app', App)
], debug=True)