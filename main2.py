from flask import Flask, render_template, request
from forms import PostForm
from model import app, blog_details13

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
    print (dir(form))

    print (form.data)


    return render_template('create_post.html', form=form, legend='Write Post today')



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080, debug=True)
