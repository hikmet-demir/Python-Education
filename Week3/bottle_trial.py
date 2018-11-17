from bottle import route, run
import random
import time
hikmet = str(33434)
hikmet = "asdasds"
@route('/hello')
def hello():
    return str(hikmet)

run(host='localhost', port=8080, debug=True, reloader=True)
