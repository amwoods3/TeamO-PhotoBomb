#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# File main

import cgitb; cgitb.enable()
import cgi
import TeamOhtml
from TeamOhtml import *

print beginHTML() + """
<tr>
<table cellpadding=5 table cellspacing="10" width=35%%>
<table align="left">
<td><a href=welcome>Home</a></td>
<td><a href=signup>Sign Up</a></td>
<td><a href=login>Log in</a></td>
</tr>
</table> </br> 
<p>

<table>
<tr>
Please enter your log in information:
<form method='post' action="home">
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
</table>
""" + endHTML()

