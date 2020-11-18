from flask import Flask, render_template

app = Flask(__name__)

@app.route("/intel")
def hello_world():
	return "Hello Everyone My name is mohit"

def sum(str1):
	return len(str1)

@app.route("/name/<my_name>")
def hello1(my_name):
	l = sum(my_name)
	return "<h1>Hello "+my_name+" lenght of name is "+str(l)+"</h1>"

@app.route("/all/<my_name>")
def all_name(my_name):
	return render_template('hello.html', name=my_name)

@app.route("/home")
def home():
	return render_template('base.html')

@app.route('/mark/<int:score>')
def score1(score):
	return render_template('mark.html', marks = score)

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=8080, debug=True)