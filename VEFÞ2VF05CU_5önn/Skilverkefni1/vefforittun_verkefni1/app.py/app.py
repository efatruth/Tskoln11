from form_skilavervefni5.bottle import *
#import os

@route("/")
def index():
    return """
    <h2>Verkefni 1</h1>
    <a href="/A">About</a>
    <a href="/B">Biography</a>
    <a href="/P">Pictures</a>
    """

@route("/A")
def about():
    return "<h3>velkominn!velkominn!!velkominn!!!</h3> í tima okkur sem er um 'ABOUT!!! <br>af About,Biography og Pictures'"

@route("/B")
def biography():
    return "<h3> velkominn til hinga!!</h3> sem um 'BIOGRAPHY!!! <br> af Biography, pictures og about' "

@route("/P")
def pictures():
    return "<h3> velkominn til að birtast 'PICTURES!!!</h3>  <br> frá Pictures,about, biography og '"

run()
#run(host='0.0.0.0', port=os.environ.get('PORT'))

