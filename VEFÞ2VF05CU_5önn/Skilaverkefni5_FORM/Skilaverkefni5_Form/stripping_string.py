from form_skilavervefni5.bottle import run, route, template, request, post


# signup
@route('/')
def index():
    return template ('signup_form.tpl')

# form process
@post('/process') # shorthand fyrir @route("/process", method="POST")
def form_process():

    # get data from input,
    name = request.forms.get('nafn')   # request.forms returns a MultiDict https://bottlepy.org/docs/dev/api.html#bottle.MultiDict


    # https://docs.python.org/3/library/html.html#html.unescape
    # name = html.escape(name)    # Convert the characters &, < and > in string s to HTML-safe sequences
    # name.strip()                # whitespace stripping, sjá einnig s.lstrip, s.rstrip

    # leið nr1. remove white space

    def clean_spaces(s):
        s = s.replace("\r", "")
        s = s.replace("\t", "")
        s = s.replace("\f", "")
        return s

    # name = clean_spaces(name)

    print(name)

    # leið nr. 2
    def sanitize(inputstr):
        sanitized = inputstr
        badstrings = [
            ';',
            '$',
            '&&',
            '../',
            '<',
            '>',
            '%3C',
            '%3E',
            '\'',
            '--',
            '1,2',
            '\x00',
            '`',
            '(',
            ')',
            'file://',
            'input://'
        ]
        for badstr in badstrings:
            if badstr in sanitized:
                sanitized = sanitized.replace(badstr, '')
        return sanitized

        #leið nr 3

        html_escape_table = {
            "&": "&amp;",
            '"': "&quot;",
            "'": "&apos;",
            ">": "&gt;",
            "<": "&lt;",
        }

        def html_escape(text):
            """Produce entities within text."""
            return "".join(html_escape_table.get(c, c) for c in text)



    return name
    # return template('signup_success.tpl', name = new_user[0])


run(host='localhost', port=8080, debug=True)
