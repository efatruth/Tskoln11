import json

from form_skilavervefni5.bottle import *

# urlopen
# lesum úr json skránni það sem er fyrir
ioStream = open('hofundar.json', 'r', encoding='utf-8')
dData = json.load(ioStream)
ioStream.close()

# basic form til að geta slegið inn nafn
@route('/')
def new():
    print(dData) # skoðum í console
    return """ 
               
                <h1>Bættu við höfund</h1>
                <form action='/add' method='get'>
                    Nafn höfundar: <input type='text' name='nafn' required>
                                 <input type='submit' value='Skrá'>
                </form>
            """
# rútína sem bætir við nafni...
@route('/add')
def add():
    # sækjum nafn  í query strenginn
    nafn = request.query.get('nafn')

    # bætum nýju nafni í dict
    dData['hofundar'].append({'nafn':nafn})
    # debug print(dData)

    # dömpum í skránna aftur, hér ætti json skrá að hafa nýtt nafn
    ioStream = open('hofundar.json','w', encoding='utf-8')
    json.dump(dData,ioStream, ensure_ascii="False")
    ioStream.close()

    print(dData) # sjáum viðbótin í JSON skrá í console

    return redirect('/')# förum á rót..

run(debug=True)
