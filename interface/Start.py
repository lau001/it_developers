def unloggedMenu():
    return ''' <div id="menu">
                    <ul>
                        <il class="button"><a href=/>Home</a></il>
                        <il class="button"><a href=/login>Login</a></il>
                        <il class="button"><a href=/signup>Sign Up</a></il>
                    </ul>
                </div>'''

def loggedMenu():
    return ''' <div id="menu">
                    <ul>
                        <il class="button"><a href=/app>Home</a></il>
                        <il class="button"><a href=/addelement>Add Element</a></il>
                        <il class="button"><a href=/seemenu>See Mc Ilcapo Menu</a></il>
                        <il class="button"><a href=/>Log Out</a></il>
                    </ul>
                </div>'''