def unloggedMenu():
    return ''' <ul>
                    <il><a href=/>Home</a></il>
                    <il><a href=/login>Login</a></il>
                    <il><a href=/signup>Sign Up</a></il>
                </ul>
                '''

def loggedMenu():
    return ''' <ul>
                    <il><a href=/app>Home</a></il>
                    <il><a href=/addelement>Add Element</a></il>
                    <il><a href=/seemenu>See Mc Ilcapo Menu</a></il>
                    <il><a href=/>Log Out</a></il>
                </ul>'''