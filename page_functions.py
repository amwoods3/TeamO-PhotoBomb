def checkLogin(user, password, userd, passd):
    if user and password and user == userd and password == passd:
        return """
        %s <a href=welcome?session=%s>click here</a> to go to the home page!
        """ % (user, user), False
    return """
    <b>Login</b>
    <form method=post action='login'>
    User Name: <input type=text name=username /></br>
    Password: &nbsp;&nsbsp;<input type=password name=password /></br>
    Do not have an account? <a href=signup>Click here</a> to register! </br>
    <input type=submit value=Submit />
    </form> """, True
