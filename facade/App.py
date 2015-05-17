import webapp2
from interface import Start
import config
from dataaccess import DataAccess
from google.appengine.api import users

class App(webapp2.RequestHandler):
    def get(self):
        self.response.write(config.htmlFirst() + Start.menu() + Start.home() + config.htmlEnd())

class SeeElements(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(config.htmlFirst() + Start.menu() + '<div>')
        SeeElements.getElementsOfType(self, "food")
        SeeElements.getElementsOfType(self, "dessert")
        SeeElements.getElementsOfType(self, "drink")
        self.response.out.write('<div>' + config.htmlEnd())

    def getElementsOfType(self, type):
        user = users.get_current_user()
        elemts = DataAccess.getElements(type)
        for ele in elemts:
            self.response.out.write('<table name="table' + ele.idElement + '"><tr>')
            self.response.out.write('<tr><td>' + ele.name + '</td><td>' + ele.price + '</td></tr>')
            self.response.out.write('<tr><td><img src="' + ele.photo + '"/></td>')
            if user == "admin":
                self.response.out.write("<td><input type='button' class='button' value='Delete' onclick=\"deleteElement(\'" + ele.idElement + "\')\"/>")
            #elif user:
            self.response.out.write("<td><input type='button' class='button' value='-' onclick=\"minusElement(\'" + ele.idElement + "\')\"/>")
            self.response.out.write('<input type="text" id="element" value=0')
            self.response.out.write("<td><input type='button' class='button' value='+' onclick=\"plusElement(\'" + ele.idElement + "\')\"/>")
            self.response.out.write('<td></tr></table>')

app = webapp2.WSGIApplication([
    ('/app', App)
], debug=True)