from form_skilavervefni5.bottle import run, route, request, response, redirect


@route('/')
def index():
        # ef það var smellt á link (þ.e. vara valin)
        if request.query.item == "parka" or request.query.item == "buxur":

            # sækjum úr get query parameter
            product = request.query.item

            # búum til cookie sem heitir vara og gefum því gildi, hvaða var smellt á
            # ath cookie sést ekki í vafra fyrr en búið er að senda hana sem request til miðlara
            # það er miðlari sem býr til cookie í vafra í response (þegar notandi er færður í /karfa)
            response.set_cookie("vara", product)

            # skoðum request sem verður sent til miðlara.
            print(response)

            # færum notanda í shopping kart
            return redirect("/karfa")

        # þessu er skilað  ef engin vara hefur verið valin ennþá.
        else:
            return """ <h1>Veldu vöru!</h1>
                        <a href="/?item=parka"> Parka úlpa </a> <br>
                        <a href="/?item=buxur"> Buxur </a>
            """


@route('/karfa')
def shopping_cart():
    # athugum hvort cookie vara er til
    if request.get_cookie("vara"):
        # sækjum úr cookie og setjum í breytu
        valin_vara = request.get_cookie("vara")
    return "Varan sem var valin: " + valin_vara


run(host='localhost', port=8080, debug=True)


"""
Ath. 
Mundu að eyða út cookies þegar þú ert að prófa þig áfram og jafnvel loka vafra.
Opnaðu Developer tools í vafra og veldu Application (chrome). Smelltu á Cookies og skoðaðu upplýsingarnar þar 
"""
