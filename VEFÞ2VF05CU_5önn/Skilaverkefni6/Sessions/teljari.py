from beaker.middleware import SessionMiddleware

from form_skilavervefni5 import bottle

session_opts = {
    'session.type': 'file',
    'session.cookie_expires': 300,
    'session.data_dir': './data',
    'session.auto': True
}
app = SessionMiddleware(bottle.app(), session_opts)

@bottle.route('/teljari')
def test():
  session = bottle.request.environ.get('beaker.session')
  session['test'] = session.get('test',0) + 1
  session.save()
  return 'Test counter: %d' % session['test']

bottle.run(app=app)