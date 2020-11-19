from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime 

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite4'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1/mohit'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)


class blog_details13(db.Model):
	blogid = db.Column(db.Integer, primary_key=True) # Automatic increment 
	blogtitle = db.Column(db.String(100), nullable=False )
	blogcontent = db.Column(db.String(500), nullable=False )
	date1 = db.Column(db.DateTime, nullable=False, default= datetime.utcnow )

	def __init__(self, blogtitle, blogcontent):
		self.blogtitle= blogtitle
		self.blogcontent = blogcontent


if __name__ =='__main__':
	db.create_all()




