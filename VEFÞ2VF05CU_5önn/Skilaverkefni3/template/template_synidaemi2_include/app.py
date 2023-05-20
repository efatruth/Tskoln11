from form_skilavervefni5.bottle import route, run, template
# coding=UTF -8
# Modular templates

# bútum vef niður í parta (skrár) með include og rebase
        # include:  includes the result of rendering another template wherever it appears in a template
        # rebase:

# master template: main layout with menu bar, footer etc.

@route("/")
def index():
        # aðskiljum gögn frá layout, notum hér dictonary fyrir gögn á vefsíðu til einföldunar.
        info = {'title': 'Modular Template',
                'content': '<p>Hello Modular templates!</p>',
                'footer': "Copyright &copy; 2017, Gunnar"
                }
        # template fallið tekur inn template skrá + gögn og skilar html.
        return template("base.tpl", info)

if __name__ == "__main__":
    run(debug=True)

