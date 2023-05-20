import json
import urllib.request

from bottle import *

info = {'title':'Elsneytis Fyrirtæki','companies':[]}

with urllib.request.urlopen("https://apis.is/petrol/") as data:
    api = json.loads(data.read().decode())
@route('/')
def front():
    info['title']='Elsneytis Fyrirtæki'

    flag = 'dud'
    for i in api['results']:
        if i['company'] !=flag:
            info['companies'].append(i['company'])
            flag = i['company']
        else:
            pass

    return template('./views/index.tpl', maininf=info,apidata=api)

@route('/<company>')
def sub_site(company):
    info ['title'] = company
    return template('./views/sub.tpl', maininf=info,apidata=api)


@route('/static/<skra>')
def static_skrar(skra):
    return static_file(skra, root='./public/')

run(host='localhost',port=8080,debug=True,reloader=True)
