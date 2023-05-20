from form_skilavervefni5.bottle import run, route, redirect

@route('/about')
def about():
    return redirect('/') # bara til að sýna redirect notkun :)
    # return "Um mig"

@route('/')
def index():
    return """<html>
                <body>
                   <a href=/about> Um mig <a>
                </body>
            </html>
    """

run()
