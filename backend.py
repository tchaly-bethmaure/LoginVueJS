from sql_tables import *
from bottle import route, run, template
from pony.orm import *
import json

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

@route('/identification/mail/<mail>/mdp/<mdp>')
def identification(mail, mdp):
	return recup_utilisateur(mail, mdp)

@db_session
def recup_utilisateur(mail, mdp):
	u = select(u for u in Utilisateur if u.mail == mail and u.password == mdp)
	if(u):
		return json.dumps(True)
	else:
		return json.dumps(False)

run(host='localhost', port=8080)