from wtforms import Form, StringField, validators, SubmitField, TextAreaField

class PostForm(Form):
	title = StringField('Title', validators=[validators.DataRequired()])
	content = TextAreaField('content', validators=[validators.DataRequired()] )
	submit = SubmitField('Post')