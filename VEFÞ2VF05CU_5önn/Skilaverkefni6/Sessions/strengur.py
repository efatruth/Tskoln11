from beaker.middleware import SessionMiddleware

from form_skilavervefni5 import bottle

# að nota sessions með Beaker
session_opts = {
    'session.type': 'memory',
    'session.cookie_expires': 300,
    'session.auto': True
}
app = SessionMiddleware(bottle.app(), session_opts)


# Dæmi um notkun
@bottle.route('/')
def session_test():
    s = bottle.request.environ.get('beaker.session')
    s['test'] = 'this string came from the session'
    s.save()
    bottle.redirect('/output')


@bottle.route('/output')
def session_output():
    s = bottle.request.environ.get('beaker.session')
    return s['test']


bottle.run(
    app=app,
    host='localhost',
    port=5000,
    debug=True,
    reloader=True
)
