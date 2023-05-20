from form_skilavervefni5.bottle import run, route, request, response

@route('/')
def index():
    if request.get_cookie("visited"):
        vafrakaka = request.get_cookie("visited")

        print(vafrakaka)
        return """<a href="/page2">go to page 2 to delete cookie</a>"""
    else:
        response.set_cookie("visited", "yes")
        return "Hello there! Nice to meet you"

@route('/page2')
def page2():
    # Að eyða cookie, yfirskrifum gildið í gildi núll og stillum tíma í fortíðina (mínustala) svo hún rennur út strax.
    response.set_cookie("visited", "", expires=0)
    return "Cookie deleted"

run(host='localhost', port=8080, debug=True)

"""
You need to refresh browser to see what happens next
"""