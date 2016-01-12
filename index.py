from bottle import route, run, template
from bottle import static_file

@route('/')
def index():
    temp_list = {
        'temperature': ["January", "February", "March", "April", "May", "June", "July"],
        'period': [28, 48, 40, 19, 96, 27, 100]
    }
    return template('index.html', temp_list=temp_list)

@route('/node/<filepath:path>')
def node_static(filepath):
    return static_file(filepath, root='./node_modules')

@route('/css/<filepath:path>')
def css_static(filepath):
    return static_file(filepath, root='./css')

@route('/js/<filepath:path>')
def js_static(filepath):
    return static_file(filepath, root='./js')


run(host="localhost", port=8080, debug=True)