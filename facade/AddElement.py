import webapp2

import re
import cgi
from interface import appInterface
from dataaccess import dataAccess
from domain import Element
import App
import config
from interface import start

class AddElement(webapp2.RequestHandler):
    def write_form(self, name="", price="", photo="", type=""):
        self.response.out.write(config.htmlFirst())
        self.response.out.write(start.loggedMenu())
        self.response.out.write(appInterface.add_element_gui() % {"name": name, "price": price, "photo":photo, "type": type})
        self.response.out.write(config.htmlEnd())
    def get(self):
        self.write_form()
    def post(self):
        idelement = dataAccess.getElementId()
        name = self.request.get("name")
        price = self.request.get("price")
        photo = self.request.get("photo")
        type = self.request.get("type")

        e = Element.make_element(idelement, name, price, photo, type)

    def escape_html(self, val):
        return cgi.escape(val, quote=True)

app = webapp2.WSGIApplication([
    ('/addelement', AddElement), ('/app', App.App)
], debug=True)