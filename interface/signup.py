import config
signup_form=config.htmlFirst() + '''<h1>Sing Up</h1>
<form method="post">
</hr>
 <table>
     <tr>
        <td class="label">Nombre de usuario </td>
        <td>
         <input type="text" name="username" value="%(username)s" placeholder="Tu nombre..."></td>
        <td class="error"> %(username_error)s</td>
    </tr>
 <tr>
 <td class="label"> Password</td>
 <td> <input type="password" name="password" value="%(password)s" autocomplete="off"></td>
 <td class="error">  %(password_error)s  </td>
 </td>
</tr>
 <tr>
 <td class="label">  Repetir Password  </td>
<td>
 <input type="password" name="verify" value="%(verify)s" placeholder="El mismo de antes">
 </td>
 <td class="error">
%(verify_error)s
 </td>
 </tr>
 <tr>
 <td class="label">
Email
 </td>
 <td>
 <input type="text" name="email"
value="%(email)s">
 </td>
 <td class="error">
%(email_error)s
 </td>
 </tr>
 </table>
 <input
type="submit"> </form>''' + config.htmlEnd()