def check_login(user, password, passd, error=''):
    if user and password and password == passd:
        return """
        %s <a href=welcome?session=%s>click here</a> to go to the home page!
        """ % (user, user)
    if password != passd and not error:
        error += "Incorrect password!!!</br>"
    return """
    <p>
    <font size="2" color="red">%s</font>
    <table>
    <tr>
    Please enter your log in information:
        <form method='post' action="login">
        <tr>
        <td>Email: </td>
        <td><input type='text' value='' name='email' /> </td></tr>
        <tr>
        <td>Password: </td>
        <td><input type='password' value='' name='password' /> </td></tr>
        <tr>
        <td></td><td align=right><input type='submit'/></td></tr>
        </tr>
        </form>
        </table>""" % error

def greet_user(user):
    return """Welcome to PhotoBomb, %s!""" % user
