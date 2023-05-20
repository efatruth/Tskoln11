#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from os import environ as env
from sys import argv

import bottle
from bottle import run, route, static_file, error, request, default_app, get, response, template, redirect
import time
import html

@route("/")
def index():
    return template('index', err=0)

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

run(host='localhost',port=8080,debug=True,reloader=True)