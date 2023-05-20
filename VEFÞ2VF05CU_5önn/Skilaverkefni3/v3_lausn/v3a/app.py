from form_skilavervefni5.bottle import route, run, template
# import os

@route("/")
def index():

    # aðskiljum gögn frá layout, notum hér dictionary (data structure) fyrir gögn á vefsíðu.
    info = {'title': 'Verkefni 3a',
            'kennitolur': ["0101010101","1234567890","1012131415"]
    }

    # sendum gögn í template
    return template("index.tpl", info)


@route("/page/<kt>")
def page(kt):

    # reiknum út þversummu kennitölu
    summa = 0
    for i in kt:
        summa = summa + int(i)

    # sendum inn kennitölu og þversummu
    return template("kennitala.tpl",kennitala=kt, summa=summa)


run(debug=True)
#run(host='0.0.0.0', port=os.environ.get('PORT'))
