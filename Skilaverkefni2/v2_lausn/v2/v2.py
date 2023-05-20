from form_skilavervefni5.bottle import route, run, abort, error, static_file, request


@route("/")
def index():
    return """
    <h2>Verkefni 2</h2>
    <a href="/a">Liður a</a>
    <a href="/b">Liður b</a>
    """

@route("/a")
def a():
    return """
    <h2>Verkefni 2A</h2>
    <a href="/sida/1">Síða 1</a>
    <a href="/sida/2">Síða 2</a>
    <a href="/sida/3">Síða 3</a>
    """

@route("/sida/<id>")
def page(id):
    if id == '1':
        return "Þetta er síða 1<br><a href='/a'>Til baka</a>"
    elif id == '2':
        return "Þetta er síða 2<br><a href='/a'>Til baka</a>"
    elif id == '3':
        return "Þetta er síða 3<br><a href='/a'>Til baka</a>"
    else:
        abort(404)

@route("/b")
def b():
    return """
    <h2>Verkefni 2B</h2>
    <h3>Veldur þinn uppáhalds bókstaf</h3>
    <a href="/sida2?bokstafur=a"><img src='myndir/a.png'></a>
    <a href="/sida2?bokstafur=b"><img src='myndir/b.png'></a>
    <a href="/sida2?bokstafur=c"><img src='myndir/c.png'></a>
    """

@route("/sida2")
def page():
    l = request.query.bokstafur
    if l == 'a':
        return "<h3>Minn uppáhalds bókstafur er:</h3><img src='myndir/a.png'>"
    elif l == 'b':
        return "<h3>Minn uppáhalds bókstafur er:</h3><img src='myndir/b.png'>"
    elif l == 'c':
        return "<h3>Minn uppáhalds bókstafur er:</h3><img src='myndir/c.png'>"
    else:
        abort(404)

@error(404)
def villa(error):
    return "<h2>Þessi síða finnst ekki, reyndu eftir</2>"

@route('/myndir/<skra>')
def static_skrar(skra):
    return static_file(skra, root='public')

run()#hægt að keyra run án parametra
#run(host='0.0.0.0', port=os.environ.get('PORT'))
