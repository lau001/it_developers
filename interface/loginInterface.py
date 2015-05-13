def loginhtml():
    return '''
            <form method="post" action=\"/login\">
                <h1>Sing Up</h1>
                </hr>
                <div> Email: <input type=\"text\" name=\"email\"/> </div>
                <div> Password: <input type=\"password\" name=\"password\"/> </div>
                <div> <input type=\"submit\" value=\"Login\"</div>
                <div> <a href="/signup">Sing Up</a><div>
            </form>'''
