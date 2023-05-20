#livinus felix bassey
#LokaverkefnI
#20.11.2018

from bottle import run, route, template, static_file, request
@route('/')
def index():
    return template('utsyn.tpl')

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./')


@route('/', method='post')
def site():
    name = request.forms.get('name')
    address = request.forms.get('address')
    phone = request.forms.get('phone')
    email = request.forms.get('email')

    return template('breytur.tpl', name=name, address=address, phone=phone, email=email)


run(host='localhost', port=8080, reloader=True, debug=True)


