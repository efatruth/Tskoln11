#!/usr/bin/env python
# -*- coding: utf-8 -*-

import html
import time

from form_skilavervefni5.bottle import run, route, static_file, request, template


@route("/")
def index():
    return template('haus.tpl', err=0)

@route('/static/<skra:path>')
def static_skrar(skra):
    return static_file(skra, root='./public/')

@route('/send', method="POST")
def sida2():
    nafn  = request.forms.get("nafn")
    heim = request.forms.get("heim")
    email = request.forms.get("email")
    simi = request.forms.get("simi")
    nam = request.forms.getall("nam")
    dagar = [request.forms.get("dag1"), request.forms.get("dag2"), request.forms.get("dag3")]

    nafn = html.escape(nafn)
    heim = html.escape(heim)

    timi = time.ctime()

    if nafn.strip() == "":
        if heim.strip() == "":
            return template('index', err=3)
        else:
            return template('index', err=1)
    elif heim.strip() == "":
        return template('index', err=2)

    return template('submit', nafn=nafn, heim=heim, email=email, simi=simi, nam=nam, timi=timi, dagar=dagar)

run(host='localhost', port=8080, debug=True,reloader=True)
