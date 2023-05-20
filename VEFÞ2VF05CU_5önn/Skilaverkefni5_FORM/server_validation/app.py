import html

from form_skilavervefni5.bottle import run, route, template, request, post, redirect


# signup
@route('/')
def index():
    return template ('signup_form.tpl')

# form process
@post('/process') # shorthand fyrir @route("/process", method="POST")
def form_process():
    # if post data is from the form, submit button
    if request.POST.get("submit","").strip():
        # get data from input,
        name = request.forms.get('nafn')
        address = request.forms.get('heimilisfang')
        email = request.forms.get('netfang')
        phone = request.forms.get('simi')
        username = request.forms.get('notandanafn')
        password = request.forms.get('lykilord')

        # validate and process input data
        # https://docs.python.org/3/library/html.html#html.unescape
        name = html.escape(name)    # Convert the characters &, < and > in string s to HTML-safe sequences
        print(name)

        # put input data in a list
        new_user=[name,address,email,phone,username,password]

        # process data and validate
        valid = True #

        if valid:
            return template('signup_success.tpl', name = new_user[0],address = new_user[1])
        else:
            return redirect("/")

run(host='localhost', port=8080, debug=True)
