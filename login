#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# File main

import cgitb; cgitb.enable()
import cgi
import TeamOhtml
import page_functions
import MySQLdb
from TeamOhtml import *
from page_functions import *


db = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="", db="PhotoBomb")

form = cgi.FieldStorage()
email = form.getfirst('email', "")
password = form.getfirst('password', "")

cursor = db.cursor()
passd = ''
error = ''
if email:
    if cursor.execute('SELECT password from User where email="%s";' % email) >= 1:
        passd = cursor.fetchone()[0]
    else:
        error = 'Email does not exist!! </br>'
print beginHTML() + top_links() + check_login(email, password, passd, error) + endHTML()

