from form_skilavervefni5.bottle import route, run, template
# coding=UTF -8
# livinus felix bassey
# Skilaverkefni3

#a. hlutir

@route("/")
def index():
        # nota hér dictonary inniheldur med lista af nöfnum og kennitölum.  .
        listanof = {'title': 'Lista af Nöfnum og Kennitölum!!',
                'content': '<p>Hello!,Velkomin til Verkefni 3!!</p>',
                'footer': "Copyright &copy; 2018, Livinus bassey"
                }
        # herna er skrá og gögn.
        return template("templete.tpl", listanof,)



@route("/kt/<id>")
def page(id):
    if id == '1':
        return "Velkomin!<br> petta er petur Allesson og<br>Þversumma kt 110193-4119 = 1+1+0+1+9+3+4+1+1+9 = 30"
    elif id == '2':
        return "Velkomin!<br> petta er Viljamu Gudmundur og<br>Þversumma kt 120293-4211 = 1+2+0+2+9+3+4+2+1+1 = 25"
    elif id == '3':
        return "Velkomin!<br> petta er Olafur Eskilisson<br>Þversumma kt 130392-4249 = 1+3+0+3+9+2+4+2+4+9 = 37"
    elif id == '4':
        return "Velkomin!<br> petta er Danna Levinson og<br>Þversumma kt 140473-2468 = 1+4+0+4+7+3+2+4+6+8 = 39"



#b. hluta

frettir = [["Irma veldur usla á Flórída", "Það er bara ... vesen á Irmu í Flórída.  Milljónir manna hafa þurft að yfirgefa heimili sin vegna yfirvofandi eyðileggingar Irmu...", "irma.jpg", "dsg@frettir.is"],
           ["Veiðin er dræm þetta haustið", "Veiðin hefur heldur verið döpur þetta haustið þrátt fyrir ágætis rigninar upp á síðkastið...", "veidi.png", "est@frettir.is"],
           ["Ólafía stendur sig vel", "Ólafía er komin í 65 sæti peningalistans og hefur því tryggt sér keppnisrétt á LPG mótaröðinni á komandi keppnistimabili...", "golf.jpeg", "htg@frettir.is"],
           ["Ísland dottið úr leik", "Íslenska karlalandsliðið í körfubolta er dottið úr leik a Eurobasket þrátt fyrir ágætis spretti inn a milli.  Ísland spilaði lokaleik sinn á mótinu fyrir troðfullri höll gegn heimamönnum Finnum..", "karfa.jpeg", "dsg@frettir.is"]]

@route("/page/<id:int>")
def index(id):
        # id vísar á þann undirlista sem við notum í template
        # búum til lýsandi breytur fyrir template (skýrara)
        return template("frett.tpl", fyrirsogn=frettir[id][0], frett=frettir[id][1], mynd = frettir[id][2], hofundur=frettir[id][3])

            # Það hefði líka verið hægt að vísa í lista úr template
            # return template("frett.tpl", frett=frettir[id])


info = {'title': 'Home',
        'content': '<p>This the front page! ... </p>',
        'about': 'Irma veldur usla á Flórída", "Það er bara ... vesen á Irmu í Flórída.  Milljónir manna hafa þurft að yfirgefa heimili sin vegna yfirvofandi eyðileggingar Irmu...", "irma.jpg", "dsg@frettir.is',
        'abouto': 'Veiðin er dræm þetta haustið", "Veiðin hefur heldur verið döpur þetta haustið þrátt fyrir ágætis rigninar upp á síðkastið...", "veidi.png", "est@frettir.is!',
        'aboutu': 'Ólafía stendur sig vel", "Ólafía er komin í 65 sæti peningalistans og hefur því tryggt sér keppnisrétt á LPG mótaröðinni á komandi keppnistimabili...", "golf.jpeg", "htg@frettir.is',
        'abouta': 'Ísland dottið úr leik", "Íslenska karlalandsliðið í körfubolta er dottið úr leik a Eurobasket þrátt fyrir ágætis spretti inn a milli.  Ísland spilaði lokaleik sinn á mótinu fyrir troðfullri höll gegn heimamönnum Finnum..", "karfa.jpeg", "dsg@frettir.is',
        'footer': "Copyright &copy; 2017, Gunnar"
        }

@route("/")
def index():
        return template("index.tpl", info)

@route("/about")
def index():
        return template("about.tpl", info)

@route("/abouto")
def index():
        return template("abouto.tpl", info)

@route("/aboutu")
def index():
        return template("aboutu.tpl", info)

@route("/abouta")
def index():
        return template("abouta.tpl", info)

if __name__ == "__main__":
    run(debug=True)


