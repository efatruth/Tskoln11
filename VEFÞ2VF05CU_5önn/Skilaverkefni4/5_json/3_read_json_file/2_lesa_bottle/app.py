import json

from form_skilavervefni5.bottle import *


# Í skránni myndir.json eru þessi gögn default ->  {"myndir": [{"mynd": "a.jpg"},{"mynd": "b.jpg"}]}
# Í rót er lesið upp úr skránni og myndum dælt á síðuna... Myndir í möppunni img

# static, til að vinna með myndir...
@route('/img/<mynd>')
def _myndir(mynd):
    return static_file(mynd, root='./img')
# default lesum myndir upp úr skrá og birtum á index.tpl, sendum niður dict->gogn
@route('/')
def index():
    ioStream = open('myndir.json','r', encoding='utf-8')
    # parsing string (JSON data) to dictionary
    dData = json.load(ioStream)
    ioStream.close()
    return template('index',gogn=dData)

run(debug=True)

"""
json.dumps(obj) -> breytir dic í streng...
json.loads(obj) -> breytir string í dict
"""
