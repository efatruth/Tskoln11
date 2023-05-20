from form_skilavervefni5.bottle import route, run, template
#coding=UTF -8
@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

run(host='localhost', port=8080)

"""
    from bottle import *
    #import os
    
    @route("/")
    def index():
        return """
        <h2>Verkefni 1</h1>
        <a href="/about">About</a>
        <a href="/bio">Biography</a>
        <a href="/pic">Pictures</a>
        """
    
    @route("/about")
    def jobs():
        return "Hér eru upplýsingar um Steve Jobs"
    
    @route("/bio")
    def jobs():
        return "Hér er Biography frá Steve Jobs"
    
    @route("/pic")
    def jobs():
        return "Hérna eru myndir frá lífi Steve Jobs"
    
    run()
    #run(host='0.0.0.0', port=os.environ.get('PORT'))
"""
