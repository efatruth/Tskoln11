import json
import urllib.request

from form_skilavervefni5.bottle import *

with urllib.request.urlopen("https://apis.is/concerts") as url:
    data = json.loads(url.read().decode())

@route('/')
def index():
    return template('index',data=data)

run(debug=True)
