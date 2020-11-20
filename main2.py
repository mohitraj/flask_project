from flask import Flask, render_template, request, redirect, url_for, jsonify
from forms import PostForm
from model import app, blog_details13, db
from flask_restful import Resource, Api

from flask import Flask, render_template,request
from werkzeug import secure_filename

api = Api(app)

#app = Flask(__name__)

@app.route('/image')
def image1():
   return render_template('image.html')


posts = [{'blogtitle':"My first post", 'blogcontent': "Hello how are you", 'date1':"2020, Nov 19" }, 
{'blogtitle':"flask project", 'blogcontent':"just do it", 'date1':"2020, Nov 19"}]

@app.route('/',methods=['GET', 'POST'] )
def display():
    posts=blog_details13.query.all()
    return render_template('display1.html', posts= posts )

@app.route("/post", methods=['GET', 'POST'])
def post1():
    print ("Hello")
    form=PostForm(request.form)
    #print (dir(form))
    if form.validate():
        post1 = blog_details13(form.title.data, form.content.data)
        db.session.add(post1)
        db.session.commit()
        return redirect(url_for('display'))


    return render_template('create_post.html', form=form, legend='Write Post today')

@app.route('/json/<id1>', methods=['GET', 'POST'])
def jsondata(id1):
    data = blog_details13.query.filter_by(blogid=id1).first()
    print (data)
    return jsonify({id1: str(data) })

class Data1(Resource):
    def get(self, id1):
        data = blog_details13.query.filter_by(blogid=id1).first()
        return {'about': str(data)}


api.add_resource(Data1, "/rest/<int:id1>")



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080, debug=True)
