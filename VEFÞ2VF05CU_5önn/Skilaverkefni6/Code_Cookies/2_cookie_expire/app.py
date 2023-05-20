import datetime

from form_skilavervefni5.bottle import run, route, request, response


@route('/')
def index():

        # búum til cookie í vafra sem heitir kaka
        # látum hana lifa í 1 dag (þó að við lokum vafra þá lifir hún áfram)
        ts = datetime.datetime.now() + datetime.timedelta(days=1)
        response.set_cookie("kaka", "sukkuladibitakaka", expires=ts)

        print(response) # skoðum request, hvað verður sent til miðlara næst.

        # sækjum gildi úr cookie eða hvað? Afhverju virkar það ekki
        kakan = request.get_cookie("kaka")  # skilar None
        print(kakan)

        return "ef við búum til cookie og á sama tíma reynum að lesa úr sama cookie þá er það ekki hægt! <br>" \
               "Það er miðlari sem býr til cookie í vafra hjá notanda, í response"


run(host='localhost', port=8080, debug=True)

"""
Response.set_cookie() tekur inn m.a. eftirfarandi færibreytur:

    max_age:    Maximum age in seconds. (default: None)
    expires:    A datetime object or UNIX timestamp. (default: None)
    domain:     The domain that is allowed to read the cookie. (default: current domain)
    path:       Limit the cookie to a given path (default: /)
    secure:     Limit the cookie to HTTPS connections (default: off).
    httponly:   Prevent client-side javascript to read this cookie (default: off, requires Python 2.6 or newer).


Ath. 
Mundu að eyða út cookies þegar þú ert að prófa þig áfram og jafnvel loka vafra.
Opnaðu Developer tools í vafra og veldu Application (chrome). Smelltu á Cookies og skoðaðu upplýsingarnar þar 
"""
