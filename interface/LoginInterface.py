def loginhtml():
    return '''
            <form method="post" action=\"/login\">
                <h1>Login</h1>
                </hr>
                <div>
                    <table>
                        <tr>
                            <td>Email</td>
                            <td><input type=\"text\" name=\"email\"/> </td>
                        <tr>
                        <tr>
                            <td>Password</td>
                            <td><input type=\"password\" name=\"password\"/></td>
                        </tr>
                    </table>
                    <input type=\"submit\" class="button" value=\"Login\"
                </div>
            </form>'''
