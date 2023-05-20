import json
import urllib.request

from bottle import *

info = {'title':'Elsneytis Fyrirtæki','companies':[],'all_prices_bensin95':[],'all_prices_diesel':[],'all_locations':[]}

with urllib.request.urlopen("https://apis.is/petrol/") as data:
    api = json.loads(data.read().decode())


flag = 'dud'
for i in api['results']:
    if i['company'] !=flag:
        info['companies'].append(i['company'])
        flag = i['company']
    else:
        pass


for i in api['results']:
    info['all_locations'].append(i['name'])


for i in api['results']:
    info['all_prices_bensin95'].append(i['bensin95'])
    info['all_prices_diesel'].append(i['diesel'])



@route('/')
def front():
    info['title']='Söluaðilar eldsneytis á íslandi'
    return template('./views/index.tpl', maininf=info,apidata=api,min_bensinprice=min(info['all_prices_bensin95']),
                    min_dieselprice=min(info['all_prices_diesel']))


@route('/<company>')
def sub_site(company):
    if company in info['companies']:
        info ['title'] = company
        return template('./views/sub.tpl', maininf=info,apidata=api,name=info['all_locations'])
    else:
        abort(404)


@route('/<company>/<location>')
def sub_sub_site(company,location):
    if location in info['all_locations']:
        info['title'] = location
        return template('./views/sub_sub.tpl', maininf=info, apidata=api,  name=info['all_locations'], company=company)
    else:
        abort(404)


@route('/static/<skra>')
def static_skrar(skra):
    return static_file(skra, root='./public/')

@error(404)
def error404(error):
    info ['title']='Error404'
    return template('./views/error.tpl',maininf=info)

run(host='localhost',port=8080,debug=True,reloader=True)
