from form_skilavervefni5.bottle import *
# import os

# datastructure, tvívíður listi
# STE Template vill fá  dictionary (breytur og 2d listar virka líka).
frettir = [
    ["Irma veldur usla á Flórída", "Það er bara helv... vesen á Irmu í Flórída.  Milljónir manna hafa þurft að yfirgefa heimili sin vegna yfirvofandi eyðileggingar Irmu...", "dsg@frettir.is", "mynd0.jpg"],
    ["Veiðin er dræm þetta haustið", "Veiðin hefur heldur verið döpur þetta haustið þrátt fyrir ágætis rigninar upp á síðkastið...", "est@frettir.is", "mynd1.jpg"],
    ["Ólafía stendur sig vel", "Ólafía er komin í 65 sæti peningalistans og hefur því tryggt sér keppnisrétt á LPG mótaröðinni á komandi keppnistimabili...", "htg@frettir.is", "mynd2.jpg"],
    ["Ísland dottið úr leik", "Íslenska karlalandsliðið í körfubolta er dottið úr leik a Eurobasket þrátt fyrir ágætis spretti inn a milli.  Ísland spilaði lokaleik sinn á mótinu fyrir troðfullri höll gegn heimamönnum Finnum..", "dsg@frettir.is", "mynd3.jpg"]
]

#rótin
@route('/')
def main():
    # sendum frettir niður sem parameter og vinnum með hann i index template-inu
    return template('index.tpl', frettir=frettir)


# Valin frétt af forsíðu, i listanum frettir (vísun á innri lista).
@route('/frett/<id:int>')
def index(id):
    # notum skýr breytuheiti uppá læsileika
    return template("frett.tpl", fyrirsogn=frettir[id][0], frett=frettir[id][1], hofundur=frettir[id][2], mynd=frettir[id][3])

@error(404)
def villa(error):
    return "<h2>Þessi síða finnst ekki, reyndu eftir</2>"


#stilla static fyrir server, setjum myndir + css skra í möppuna static
@route('/static/<skra>')
def static_skrar(skra):
    return static_file(skra, root='./static/')

run(debug=True)
#run(host='0.0.0.0', port=os.environ.get('PORT'))
