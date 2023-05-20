import json

from form_skilavervefni5.bottle import route, run, template


# Í skránni gengi.json eru eftirfarandi gögn:
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

@route('/')
def index():
  # Tengjumst við skránna gengi.json
  ioStream = open('gengi.json','r', encoding='utf-8')
  data = json.load(ioStream)
  ioStream.close()

  return template('index', gengi=data)

run(debug=True)


"""
Önnur leið að sækja JSON skrá:

  with open("bekkur.json","r") as skra:
    gogn = json.load(skra)

We can use with statement in Python such that we don’t have to close the file handler. 
The with statement creates a context manager and it will automatically close the file handler for you when you are done with it.
"""
