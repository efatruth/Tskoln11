from form_skilavervefni5.bottle import run, route, request, post

@post('/saveList') # eða svona @route('/saveList', method='POST')
def save_list():
    forms = request.forms.getall('the_list')
    print(forms)    # see list in console
    # return forms[0]     # returns first selected value in list (it can be any value in select element in form)
    return forms # returns all selected items in list

@route('/')
def index():
    return """<html>
                <body>
                    <form method="post" action="/saveList">
                        <!-- we can select multiple items -->
                        <h1>Select one or more items in list and press submit!<h1>
                         <select multiple="multiple" id="the_list" name="the_list">
                             <option value="1">Item 1</option>
                             <option value="2">Item 2</option>
                             <option value="3">Item 3</option>
                         </select>
                        <input type="submit" />
                     </form>
                </body>
            </html>
    """

run(debug=True)
