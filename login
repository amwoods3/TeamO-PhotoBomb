#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# File main

import cgitb; cgitb.enable()
import cgi
import TeamOhtml
from TeamOhtml import *

print beginHTML() + """
<table>
<form method='post' action="home">
<tr>
<td>Email</td>
<td><input type='text' value='' name'email' /> </td></tr>
</tr>
</form>
</table>
""" + endHTML()

