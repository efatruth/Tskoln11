#livinus felix bassey
#Skilaverkefn7
#20.11.2018

from bottle import request, route, static_file, run, template, redirect
import pymysql

connection = pymysql.connect(host="tsuts.tskoli.is",
                     user="0301865919",
                     passwd="mypassword",
                     db="0301865919_verk7",
                     charset='utf8mb4',
                     cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:

        # Create a new record
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('gjg@tskoli.is', '123'))

    # connection is not autocommit by default. So you must commit to save your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('gus@tskoli.is',))
        result = cursor.fetchone()

        # view record
        print(result)
finally:
    connection.close()

@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='./static/')

@route('/')
def index():
    return template('forsida.tpl')

@route('/signin')
def sign_in():
    return template('sign_in.tpl')

@route('/signin', method='POST')
def sign_in_info():
    cur = db.cursor()

    number_of_rows = cur.execute('SELECT * FROM USER')

    users = cur.fetchall()

    notenda_listi = []
    for i, x in users:
        notenda_listi.append([i, x])
    signinUser = request.forms.get('SignIn_username')
    signinPass = request.forms.get('SignIn_password')

    signIn = list((signinUser, signinPass))

    for notandanafn, lykilord in notenda_listi:
        if signIn[0] == notandanafn and signIn[1] == lykilord:
            redirect('/leyni')
            break
    else:
        return template('sign_in_error.tpl', message="Innskráning hefur ekki staðist")


@route('/signup')
def sign_up():
    return template('sign_up')

@route('/signup', method="POST")
def sign_up_info():
    cur = db.cursor()

    number_of_rows = cur.execute('SELECT * FROM USER')

    users = cur.fetchall()

    notenda_listi = []
    for i, x in users:
        notenda_listi.append([i, x])
    signupUser = request.forms.get('SignUp_username')
    signUpPass = request.forms.get('SignUp_password')

    signUp = list((signupUser, signUpPass))

    for notendanafn, lykilord in notenda_listi:
        if signUp[0] != notendanafn:
            try:
                number_of_rows = cur.execute('INSERT INTO USER VALUES(%s, %s)', (signupUser, signUpPass))
                db.commit()
                redirect('/success')
            except (pymysql.IntegrityError):
                return template('sign_up_error', message="Nýskráning hefur ekki staðist")

@route('/leyni')
def secret_site():
    return template('leyni.tpl')

@route('/success')
def sign_up_success():
    return template('sign_up_success', message="Nýskráning hefur staðist")


run(host='localhost', port=8080, reloader=True, debug=True)

if count == 1:
    print(stafir[0]*count)
count += 1

if count == 6:
    count = 1

