#!/usr/bin/env python
# -*- coding: utf-8 -*-

import bottle
import pymysql
from beaker.middleware import SessionMiddleware


"""
Búum til MySQL gagnagrunn (ein tafla) á miðlara t.d. á tsuts.tskoli.is  

    CREATE TABLE `users` (
        `id` int(11) NOT NULL AUTO_INCREMENT,
        `name` varchar(255) COLLATE utf8_bin NOT NULL,
        `email` varchar(255) COLLATE utf8_bin NOT NULL,
        `password` varchar(255) COLLATE utf8_bin NOT NULL,
        PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin
    AUTO_INCREMENT=1;
"""

# Configure the SessionMiddleware, Beaker
session_opts = {
    'session.type': 'memory',
    'session.cookie_expires': 300,
    'session.auto': True
}
# a replacement of original application app.py
app = SessionMiddleware(bottle.app(), session_opts)

# Skráningarform
@bottle.route('/')
@bottle.get('/signup')
def signup():
    return bottle.template('signup')

# Skráning í db
@bottle.post('/register')
def do_register():

    # sækjum gögn úr forminu.
    name = bottle.request.forms.get('name')
    email = bottle.request.forms.get('email')
    password = bottle.request.forms.get('password')
    # Sleppum e. filtera og e. validate gögn úr forminu, til einföldunar.

    try:
        # Connect to the database, cursorclass tryggir að við fáum data í dictionary
        connection = pymysql.connect(host='tsuts.tskoli.is',
                                         user='0301865919',
                                         password='mypassword',
                                         db='0301865919_verk7',
                                         charset='utf8mb4',
                                         cursorclass=pymysql.cursors.DictCursor)

        # Búum til cursor til að keyra fyrirspurnir.
        with connection.cursor() as cursor:

            # komum í veg fyrir tvísrkáningu á username, gerum fyrirspurn í db áður en við skrifum notanda í db.
            sql = "SELECT `email` FROM `users` WHERE `email`=%s"
            cursor.execute(sql,email)
            result = cursor.fetchone() # fáum dictionary (þægilegra en tuple)

            if result == None:
                # skrifum notanda í db
                sql2 = "INSERT INTO `users` (`name`, `email`, `password`) VALUES (%s, %s, %s)"
                cursor.execute(sql2,(name, email, password))
                connection.commit()
                bottle.redirect('/login')
            else:
                return "Netfang er þegar í notkun, reyndu aftur"
    finally:
        cursor.close() # Closing a cursor just exhausts all remaining data.
        connection.close() # lokum db tengingu


# innskráning
@bottle.get('/login') # or @route('/login')
def login():
    return bottle.template('innskra')

@bottle.post('/login') # eða @route('/login', method='POST')
def do_login():
    username = bottle.request.forms.get('username')
    password = bottle.request.forms.get('password')

    # Athugum hvort notandi sé í gagnagrunni.
    try:
        # Connect to the database, cursorclass tryggir að við fáum data í dictionary
        connection = pymysql.connect(host='tsuts.tskoli.is',
                                     user='0301865919',
                                     password='mypassword',
                                     db='0301865919_verk7',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)

        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `id`,  `name`, `email`, `password` FROM `users` WHERE `email`=%s AND `password`=%s"
            cursor.execute(sql, (username, password))
            result = cursor.fetchone()
            print(result) # dictionary, gögn úr db.

    finally:
        cursor.close()
        connection.close()

    # Ef notandi er ekki í db.
    if result is None:
        return "Notandi er ekki til."
    else:
        # setjum nafn í cookie til að nota í admin vefsíðu
        bottle.response.set_cookie("name", result["name"])

        # skrifum í session skrá, admin check
        session = bottle.request.environ.get('beaker.session')
        session['username'] = 'username'
        session.save()

        # redirect method sends a 303 response to the user, who will then send another request to your server for the '/restricted' page
        bottle.redirect('/restricted?username=username')

@bottle.route('/restricted')
def admin():
    # sækjum query parameter
    username= bottle.request.query.username

    # authentication
    if username in bottle.request.environ.get('beaker.session'):
        # sækum cookie og birtum nafn í admin vefsíðu.
        name = bottle.request.get_cookie("name")
        return bottle.template('admin', name=name)
    else:
        return "Access denied."

@bottle.route('/logout', method=["GET", "POST"])
def logout():
        session = bottle.request.environ.get('beaker.session')
        # session delete method deletes the session from the back-end storage and sends an expiration on the cookie requesting the browser to clear it
        session.delete()
        # delete cookie
        bottle.response.set_cookie("name", "", expires=0)
        bottle.redirect('/login')



@bottle.route('/static/<filename>')
def server_static(filename):
    return bottle.static_file(filename, root='./static')

bottle.run(
    app=app,
    host='localhost',
    port=8080,
    debug=True
)
