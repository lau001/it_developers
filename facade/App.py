import webapp2

class App(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        self.response.write("Hello there!")


app = webapp2.WSGIApplication([
    ('/app', App)
], debug=True)