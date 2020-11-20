from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_dance.contrib.github import make_github_blueprint, github

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite4'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1/mohit'
app.config['SECRET_KEY'] = "random string"

github_blueprint= make_github_blueprint(client_id='75d9c240a109aec94d37', client_secret='1dc7e808917087f982a4238478c305ef8d2c18c4')


app.register_blueprint(github_blueprint,url_prefix='/github_login')

@app.route('/github')
def github_login():
	if not github.authorized:
		return redirect(url_for('github.login'))
	account_info = github.get('/user')

	if account_info.ok:
		account_info_json = account_info.json()
		return '<h1> Your github name {}'.format(account_info_json['login'])

	return '<h1> Request </h1>'



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080, debug=True)