#livinus felix bassey
#Skilaverkefni2 í vefforritun
#30.08.2018

import os

from form_skilavervefni5.bottle import route, run, abort, error, static_file, request


@route("/")
def index():
    return """
    <h2>Velkomin í Verkefni 2</h2>
    <a href="/a">Liður a</a><br>
    <a href="/b">Liður b</a>
    """

@route("/a")
def a():
    return """
    <h2>Verkefni 2A</h2>
    <a href="/sida/1">Hér er BLAÐSÍÐA 1</a><br>
    <a href="/sida/2">Hér er BLAÐSÍÐA 2</a><br>
    <a href="/sida/3">Hér er BLAÐSÍÐA 3</a>
    """

@route("/sida/<id>")
def page(id):
    if id == '1':
        return "goddaginn!! við erum í síðu 1<br><a href='/a'>Til baka</a>"
    elif id == '2':
        return "goddaginn!! við erum í síðu 3<br><a href='/a'>Til baka</a>"
    elif id == '3':
        return "goddaginn!! við erum í síðu 3<br><a href='/a'>Til baka</a>"
    else:
        abort(404)

@route("/b")
def b():
    return """
    <h2>Verkefni 2B</h2>
    <h3>Veldur þinn mynd sem er :labba,fara eða avextir</h3>
    <a href="/sid2?ord=a"><img src='myndir/afara.png'></a>
    <a href="/sid2?ord=b"><img src='myndir/bavextir.png'></a>
    <a href="/sid2?ord=c"><img src='myndir/clabba.jpg'></a>
    """

@route("/sid2")
def page():
    l = request.query.ord
    if l == 'a':
        return "<h3>Minn uppáhalds mynd er:</h3><img src='myndir/afara.png'>"
    elif l == 'b':
        return "<h3>Minn uppáhalds mynd er:</h3><img src='myndir/bavextir.png'>"
    elif l == 'c':
        return "<h3>Minn uppáhalds mynd er:</h3><img src='myndir/clabba.jpg'>"
    else:
        abort(404)

@error(404)
def villa(error):
    return "<h2>Þessi síða finnst ekki, reyndu eftir</2>"

@route('/myndir/<skra>')
def static_skrar(skra):
    return static_file(skra, root='Skilaverkefni2_myndir')


run(host='0.0.0.0', port=os.environ.get('PORT'),reloder=True)
