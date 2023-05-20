from form_skilavervefni5.bottle import route, run, template
# coding=UTF -8
# við getum notað python (template functions) í bland við html til að fá það view sem við viljum
# template dregur úr strengjavinnslu.

# sýnidæmi 1
@route("/page1")
def index():
        # skilar og renderar index1.tpl (template skrá) sem er í view möppu (bara uppá skipulag)
        # sýnir if else notkun
        return template("index1.tpl")

# sýnidæmi 2
@route("/page2")
def index2():
        # sýnir for lykkju notkun
        return template("index2.tpl")

# sýnidæmi 3
@route("/page3")
def index3():
        # sendir inn breytu í template sem það notar
        return template("index3.tpl", name="Gunnar")

# sýnidæmi 4
@route("/page4")
def index4():
        # aðskiljum gögn frá layout, notum hér dictonary
        my_dict = {'number': '123', 'street': 'Fake St.', 'city': 'Fakeville'}
        # template tekur inn template skrá og gögn og blandar saman.
        return template("index4.tpl", my_dict)

# sýnidæmi 5
@route("/page5")
def index5():
        info = {'title': 'The Beatles',
                'names': ['John', 'Paul', 'George', 'Ringo']
        }
        # template fallið tekur inn template skrá + gögn og skilar html.
        return template("index5.tpl", info)


# keyrum upp localhost
if __name__ == "__main__":
    run(debug=True)

"""
Athugasemdir:

    HTML special characters are escaped automatically to prevent XSS attacks.

        template('Hello {{name}}!', name='<p>hello world</p>')
        '&lt;p&gt;hello world&lt;/p&gt;'        
        
        Við getum farið framhjá þessu með að nota ! í expressio
        template('Hello {{!name}}!', name='<p>World</p>')


"""
