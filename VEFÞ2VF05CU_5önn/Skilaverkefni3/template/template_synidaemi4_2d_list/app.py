from form_skilavervefni5.bottle import route, run, template
# coding=UTF -8

@route("/")
def index():
    # data
    blog = [['2007/03/13', 'Steve', '<p>Nothing happened today.</p>'],
            ['2007/03/12', 'John', '<p>Something happened today.</p>'],
            ['2007/03/11', 'Steve', '<p>Welcome to the new blog!</p>']]

    return template("blogpost.tpl", posts = blog)

if __name__ == "__main__":
    run(debug=True)

# {{!content}} til að nota html markup
