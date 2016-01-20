from bottle import route, run, template
from bottle import static_file
import dbaccess
import subprocess
import hydro_ctl


@route('/')
def index():
    dbo = dbaccess.DbOperation()
    temp_list = dbo.selectRecord(7, 0)
    dbo.connectionClose()
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


@route('/start')
def startMain():
    ctl = hydro_ctl.HydroControl()
    ctl.startMain()
    return 'start'


@route('/stop')
def stopMain():
    ctl = hydro_ctl.HydroControl()
    ctl.stopMain()
    return 'stop'


cmd = 'hostname'
p = subprocess.check_output(cmd)
name = str(p, encoding='utf-8')
run(host=name.rstrip(), port=8080, debug=True)