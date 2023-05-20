# livinus felix bassey
# vefforritun1
# 21.09.2018


import json
import urllib.request

from form_skilavervefni5.bottle import *

with urllib.request.urlopen("http://apis.is/currency/m5") as url:
    data = json.loads(url.read().decode())

@route('/')
def index():
    return template('currency',data=data)

run(debug=True)
