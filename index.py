from bottle import route, run, template
from bottle import static_file

@route('/')
def index():
    return template('index.html')

@route('/node/<filepath:path>')
def node_static(filepath):
    return static_file(filepath, root='./node_modules')

@route('/css/<filepath:path>')
def css_static(filepath):
    return static_file(filepath, root='./css')


run(host="localhost", port=8080, debug=True)