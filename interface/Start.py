from google.appengine.api import users

def menu():
    user = users.get_current_user()
    # unlogged user
    if not user:
        return ''' <div id="menu">
                        <ul>
                            <il class="button"><a href=/>Home</a></il>
                            <il class="button"><a href=/login>Login</a></il>
                            <il class="button"><a href=/signup>Sign Up</a></il>
                        </ul>
                    </div>'''

    # logged user
    else:
        menu1 = ''' <div id="menu">
                        <ul>
                            <il class="button"><a href=/>Home</a></il>
                            <il class="button"><a href=/seemenu>See Mc Ilcapo Menu</a></il>
                            '''

        # ADMIN MENU
        if user == "admin":
            menu2 = '''     <il class="button"><a href=/addelement>Add Element</a></il>'''
        # USER MENU
        else:
            menu2 = '''     <il class="button"><a href=/order>Your order</a></il>'''

        menu3 = "         <il class=\"button\"><a href=\"%s\">Logout</a></il> </ul></div>" % users.create_logout_url("/")

        return menu1 + menu2 + menu3

def home():
    user = users.get_current_user()
    if user:
        return "<h1>Home, welcome, %s!</h1>" % users.get_current_user()
    else:
        return "<h1>Home</h1>"

def aboutus():
    return "<p> This is a web project developed by two students from the Computer Science" \
           " Engineering degree of the University of the Basque Country. This web is " \
           " meant to simulate a restaurant's website where you can see the menu and " \
           " order some food.</p>"