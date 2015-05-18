import webapp2
from dataaccess import DataAccess
from google.appengine.api import users


def menu(self):

    logged = self.request.cookies.get("logged")

    # logged user
    if logged == "true":

        menu1 = ''' <div id="menu">
                        <ul>
                            <il class="button"><a href=/>Home</a></il>
                            <il class="button"><a href=/menu>Menu</a></il>
                            <il class="button"><a href=/logout>Logout</a></il>
                            '''

        # ADMIN MENU
        username = self.request.cookies.get("username")
        useradmin = False
        name = DataAccess.Usuario.name
        usuario = DataAccess.Usuario.query(name == username)
        if usuario.count() == 1:
            for aux in usuario:
                useradmin = aux.admin

        if useradmin == True:
            menu2 = '''     <il class="button"><a href=/addelement>Add Element</a></il>'''
        # USER MENU
        else:
            menu2 = ''''''

        return menu1 + menu2

    else:
         return ''' <div id="menu">
                        <ul>
                            <il class="button"><a href=/>Home</a></il>
                            <il class="button"><a href=/login>Login</a></il>
                            <il class="button"><a href=/signup>Sign Up</a></il>
                            <il class="button"><a href=/menu>Menu</a></il>
                        </ul>
                    </div>'''

def home():
    logged = self.request.cookies.get("logged")
    if logged=="true":
        username = self.request.cookies.get("username")
        return "<h1>Home, %s!</h1>" % username
    else:
        return "<h1>Home</h1>"

def aboutus():
    return "<p> This is a web project developed by two students from the Computer Science" \
           " Engineering degree of the University of the Basque Country. This web is " \
           " meant to simulate a restaurant's website where you can see the menu and " \
           " order some food.</p>"
