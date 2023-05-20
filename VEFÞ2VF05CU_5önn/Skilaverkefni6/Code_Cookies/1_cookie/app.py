from form_skilavervefni5.bottle import run, route, request, response

@route('/')
def hello_again():
    # athugum hvort cookie með heitinu visited sé til
    # notandi gæti hafið beytt eða eytt cookie gildum, eða útrunnið
    if request.get_cookie("visited"):
        # lesum gildið (yes) úr cookie
        visited = request.get_cookie("visited")
        return visited + " welcome back! <br> Nice to see you again"
    else:
        # býr til cookie í vafra sem heitir visited með gildinu yes
        response.set_cookie("visited", "yes")
        return "Hello there! Nice to meet you"

run(host='localhost', port=8080, debug=True)

"""
Cookies:
 * cookie expires at the end of the browser session or as soon as the browser window is closed. 
 * Cookies are limited to 4 KB of text in most browsers.
 * Some users configure their browsers to not accept cookies at all. Most search engines ignore cookies too. Make sure that your application still works without cookies.
 * Cookies are stored at client side and are not encrypted in any way. Whatever you store in a cookie, the user can read it. Worse than that, an attacker might be able to steal a user’s cookies through XSS vulnerabilities on your side. Some viruses are known to read the browser cookies, too. Thus, never store confidential information in cookies.

    1. Prófaðu að nota refresh í vafra og sjáðu hvað gerist
    2. Prófaðu að opna annan vafra og sjáðu hvað gerist
    3. lokaðu vafra og opnaðu aftur og sjáðu hvað gerist
    4. Opnaðu Developer tools í vafra og veldu Application (chrome). Smelltu á Cookies og skoðaðu upplýsingarnar þar
       prófaðu að eyða cookie þar og smelltu á refresh.
"""
