def check_login(user, password, passd):
    if user and password and password == passd:
        return """
        %s <a href=welcome?session=%s>click here</a> to go to the home page!
        """ % (user, user)
    return """
    <p>
    
    <table>
    <tr>
    Please enter your log in information:
        <form method='post' action="login">
        <tr>
        <td>Email: </td>
        <td><input type='text' value='' name'email' /> </td></tr>
        <tr>
        <td>Password: </td>
        <td><input type='password' value='' name'password' /> </td></tr>
        <tr>
        <td></td><td align=right><input type='submit'/></td></tr>
        </tr>
        </form>
        </table>"""

def greet_user(user):
    return """Welcome to PhotoBomb, %s!""" % user
