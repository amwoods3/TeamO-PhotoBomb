def beginHTML():
    return """Content-Type: text/html;charset=utf-8

    <a href=welcome style="text-decoration:none">
    <h3 align="Center"> <font size="7" color="black">Photo Bomb!</font> </h3>
    </a>
    <hr>
    <html>
    <body style="background-color:Beige">
    

    """

def endHTML():
    return """
    </body>
    </html>
    """

def top_links():
    return """ 
    <tr>
    <table cellpadding=5 table cellspacing="10" width=35%%>
    <table align="left">
    <td><a href=welcome>Home</a></td>
    <td><a href=signup>Sign Up</a></td>
    <td><a href=login>Log in</a></td>
    </tr>
    </table> </br> """
