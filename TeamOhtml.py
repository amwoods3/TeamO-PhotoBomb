def beginHTML():
    return """Content-Type: text/html;charset=utf-8
    
    <h3 align="Center"> <font size="7" color="black">Photo Bomb!</font> </h3>
    <hr>
    <html>
    <body style="background-color:Beige">
    

    """

def endHTML():
    return """
    </body>
    </html>
    """

def top_links(user_name=''):
    if not user_name:
        return """ 
        <tr>
        <table cellpadding=5 table cellspacing="10" width=35%%>
        <table align="left">
        <td><a href=welcome>Home</a></td>
        <td><a href=signup>Sign Up</a></td>
        <td><a href=login>Log in</a></td>
        <td><a href=viewListOfUsers>View List of Users</a></td>
        </tr>
        </table> </br> """
    else:
        return """ 
        <tr>
        <table cellpadding=5 table cellspacing="10" width=35%%>
        <table align="left">
        <td><a href=home?session=%s>Home</a></td>
        <td><a href=settings?session=%s>Settings</a></td>
        <td><a href=upload?session=%s>Upload an Image</a></td>
        <td><a href=viewPhotos?session=%s>View My Photos</a></td>
        <td><a href=viewListOfUsers?session=%s>View List of Users</a></td>
        <td><a href=welcome>Log Out</a></td>
        </tr>
        </table> </br> """ % (user_name, user_name, user_name, user_name, user_name)
