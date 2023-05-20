from form_skilavervefni5.bottle import route, run, template, request

"""
form
"""
# form
@route("/")
def index():
        return template("index.tpl")

# formvinnsla, vinnum með gögn (e. input) frá formi
# skrifum method POST til að fá aðgang að post gögnum
@route("/send", method="POST")
def form_process():
        # sækjum streng/gildi úr input frá formi. Við notum name breytu í formi sem teningu.
        firstname = request.forms.get("firstname")
        lastname =  request.forms.get("lastname")

        # heppilegra að nota template
        return "<p>" + firstname + " " + lastname + "</p>"

if __name__ == "__main__":
    run(debug=True)
