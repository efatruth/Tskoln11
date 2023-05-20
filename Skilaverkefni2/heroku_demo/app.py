#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv

from form_skilavervefni5 import bottle
from form_skilavervefni5.bottle import *

bottle.debug(True)

@get('/')
def index():
    return "Hallo Heimur í Heroku og Github"

bottle.run(host='0.0.0.0', port=argv[1])
