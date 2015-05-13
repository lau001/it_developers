from google.appengine.api import users

import config


user = users.get_current_user()
        
if user:
    msg = ("Welcome, %s! (<a href=\"%s\">logout</a></br><a href=\"/app\"> app </a>)" % (user.nickname(), users.create_logout_url("/")))
else:
    msg = ("<form action=\"/signup\">" +
           "<input type=\"submit\" value=\"Sign Up\">" +
            "</form>")

startapp = config.htmlFirst() + \
    ''' <div> <h1>Welcome!</h1> </div> ''' + \
        msg + config.htmlEnd()



