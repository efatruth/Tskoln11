from form_skilavervefni5.bottle import run, route, static_file
# Sýnidæmi um hvernig hægt er að tengja CSS skrá og mynd við vef.

# Vefsiða með CSS og mynd.
@route('/')
def index():
    return '''
            <!DOCTYPE html>
            <html>
                <head>
                    <title>Hello world</title>
                    <meta charset="utf-8">
                    <!-- notum route sem heitir static og slóðina css/styles.css í public möppu -->
                    <link rel="stylesheet" href="./static/css/styles.css">
                </head>
                <body>
                    <h1>Halló heimur í bláum lit með CSS!</h1>
                    <!-- notum route sem heitir static og slóðina img/logo.png í public möppu -->
                    <img src="./static/img/logo.png" alt="Bottle logo">
                </body>
            </html>
        '''

# stilla route með path svo við getum vísað í undirmöppur með static skrár (myndir og css)
@route('/static/<skra:path>')
def static_skrar(skra):
    # root geymir slóð að skrám
    # path möguleikar: root = "./static" root = "static" root = "/static"
    return static_file(skra, root='./public/')

run(host='localhost', port=8080, debug=True)




"""

Útskýringar:

    Static Files (css, myndir ogsfrv.):  http://bottlepy.org/docs/dev/tutorial.html#tutorial-static-files
    
    Static files such as images or CSS files are not served automatically.
    You have to add a route and a callback to control which files get served and where to find them:   
   
    static_file()
            This function is a helper to serve files in a safe and convenient way.
            It automatically guesses a mime-type, adds a Last-Modified header,
            restricts paths to a root directory for security reasons and generates appropriate error responses
            (403 on permission errors, 404 on missing files).
        
    return static_file(filename, root='/path/to/your/static/files')


Aðrar athugasemdir: 

    Vafrar nota Cache til að geyma t.d. myndir í minni.
    það þarf að hafa þetta í huga þegar verið er að prófa kóða (clear cache) 

"""
