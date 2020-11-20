from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<html><body><h1>Hello, Mohit!</h1></body></html>'


@app.route('/name/<my_name>')
def all_name(my_name):
    str1 = f"<html><body><h1>Hello {my_name}</h1></body></html>"
    return str1

@app.route('/sq/<int:a>')
def square(a):
    return "Square "+str(a**2)


@app.route('/name/<name>/<int:a>')
def data(name,a):
    return name+ str(a)

@app.route('/name1/<my_name>')
def style_name(my_name):
    return "<htm><body><h1>"+my_name+"</h1></body>  </html>"




if __name__ == '__main__':
    app.run(debug=True)
