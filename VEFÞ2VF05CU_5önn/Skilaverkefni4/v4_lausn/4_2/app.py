import json
import urllib.request

from form_skilavervefni5.bottle import route, run, template

# http://docs.apis.is/#endpoint-currency
#  { "results": [
#   {
# 		"shortName": "USD",
# 		"longName": "Bandarískur dalur",
# 		"value": 113.45,
# 		"askValue": 0,
# 		"bidValue": 0,
# 		"changeCur": 0.07,
# 		"changePer": 0.06
# 	} ...

with urllib.request.urlopen("https://apis.is/currency/") as url:
    apidata = json.loads(url.read().decode())

@route('/')
def index():
  return template('index', gengi=apidata)

run(debug=True)
