import webapp2
import cgi
from interface import AppInterface
from dataaccess import DataAccess
import App
import config
from interface import Start

class AddElement(webapp2.RequestHandler):
    def write_form(self, name="", price="", photo="", type=""):
        self.response.out.write(config.htmlFirst())
        self.response.out.write(Start.menu())
        self.response.out.write(AppInterface.add_element_gui() % {"name": name, "price": price, "photo": photo, "type": type})
        self.response.out.write(config.htmlEnd())
    def get(self):
        self.write_form()
    def post(self):
        element_idelement = DataAccess.getLastElementId()
        element_name = self.request.get("name")
        element_price = self.request.get("price")
        element_photo = self.request.get("photo")
        element_type = self.request.get("type")


        # STORE ELEMENT
        element = DataAccess.Elemento.query(element_idelement == DataAccess.Elemento.idElement)
        if element.count() == 0:
            e = DataAccess.Elemento()
            e.idElement = element_idelement
            e.name = element_name
            e.type = element_type
            e.price = element_price
            e.photo = element_photo
            e.put()

    def escape_html(self, val):
        return cgi.escape(val, quote=True)

app = webapp2.WSGIApplication([
    ('/addelement', AddElement),
    ('/app', App.App)
], debug=True)