from form_skilavervefni5.bottle import route, static_file, run

# Sýnidæmi um hvernig hægt er að tengja CSS skrá og mynd við vef.
@route('/')
def index():
    return '''
            <!DOCTYPE html>
            <html>
                <head>
                    <title>Hello world</title>
                    <meta charset="utf-8">
                    <!-- css er að finna í undirmöppunni css-->
                    <link type="text/css" href="/static/main.css" rel="stylesheet">
                </head>
                <body>
                    <h1>Rauður litur með CSS?</h1>
                    <p>Route með regex til að vinna með static skrár!</p>
                    <!-- mynd er að finna í undirmöppunni img-->
                    <img src="/static/python-logo.png" alt="Bottle">
                </body>
            </html>
        '''

# Við getum einnig notað regex til að filtera nákvæmlega þær skrár sem við viljum vinna með.

# CSS skrár.  Leitar að öllum css skráarheitum í css undir möppunni á vefrót
@route('/static/<filename:re:.*\.css>')
def send_css(filename):
    # css directory
    return static_file(filename, root='public/css')


# PNG skrár eingöngu í undirmöppunni img
@route('/static/<filename:re:.*\.png>')
def send_image(filename):
    # img directory
    return static_file(filename, root='public/img', mimetype='image/png')


run(host='localhost', port=8080, debug=True)
