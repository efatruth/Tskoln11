from form_skilavervefni5.bottle import run, route, request


@route('/process', method='POST')
def process_form():
    form_list = request.forms.getall('interest')
    print(form_list)    # see list in console
    return form_list    # returns all selected items in list, you should use a loop to work with items from list


@route('/')
def index():
    return """  <h1> Handling multiple checkboxes </h1>
                <form action="/process" method="post">
                    <fieldset>
                      <legend>Choose your interests</legend>
                      <div>
                        <input type="checkbox" id="coding" name="interest" value="coding">
                        <label for="coding">Coding</label>
                      </div>
                      <div>
                        <input type="checkbox" id="music" name="interest" value="music">
                        <label for="music">Music</label>
                      </div>
                    </fieldset>     
                    <button type="submit">Select</button>
                </form>
    """

run()
