from form_skilavervefni5.bottle import route, run, template
# coding=UTF -8

"""
Master template (base.tpl), all pages will use the same overall page layout with the standard stylesheet, page menu and footer.
Other templates (about.tpl, index.tpl) then specialise this to add new parts using rebase
"""
# aðskiljum gögn frá layout, notum hér dictonary fyrir gögn á vefsíðu til einföldunar.
info = {'title': 'Home',
        'content': '<p>This the front page! ... </p>',
        'about': 'My name is Gunnar and I am teacher!',
        'footer': "Copyright &copy; 2017, Gunnar"
        }

@route("/")
def index():
        return template("index.tpl", info)

@route("/about")
def index():
        return template("about.tpl", info)

if __name__ == "__main__":
    run(debug=True)

"""
Mockup:
When you are designing a page layout for a website it is common (easier) to mock up your page design as a static HTML page.
then turn these into templates that your application can use to generate the final HTML. 
"""
