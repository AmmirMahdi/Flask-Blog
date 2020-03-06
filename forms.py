from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, BooleanField, 
                    SubmitField,IntegerField,DateTimeField,
                    TextAreaField,validators)
from wtforms.validators import DataRequired



class PostForm(FlaskForm):

    """
    
    id          = db.Column(db.Integer, primary_key=True)
    title       = db.Column(db.String, unique=True, nullable=False)
    author      = db.Column(db.String, db.ForeignKey('author.id'))
    created     = db.Column(db.DateTime)
    body        = db.Column(db.Text)
    updated     = db.Column(db.DateTime)
    post        = db.relationship('Comment', backref='post',lazy=True)

    """

    # id = IntegerField("p")
    title   = StringField("post title")
    author  = IntegerField("ID AUTHOR")
    created = DateTimeField('Which date is your favorite?', format='%m/%d/%y', validators=[DataRequired()])
    body    = TextAreaField("Body")
    updated = DateTimeField('Which date is your favorite?', format='%m/%d/%y', validators=[DataRequired()])
    submit  = SubmitField("Submit")


class AddComment(FlaskForm):
    """
     id     = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String, db.ForeignKey('author.id'))
    post   = db.Column(db.String, db.ForeignKey('post.id'))
    body   = db.Column(db.Te
    """
    author = IntegerField("Author ID")
    post   = IntegerField("Post   ID")
    body   = TextAreaField("enter commnet")
    submit = SubmitField("Submit")


class AddAuthor(FlaskForm):
    """
      
    id        = db.Column(db.Integer, primary_key=True)
    name      = db.Column(db.String, unique=True, nullable=False)
    family    = db.Column(db.String)
    email     = db.Column(db.DateTime)
    password  = db.Column(db.Text)
    user    = db.relationship('User',backref='author',lazy=False)


    """
    name = StringField("author name ")
    family = StringField("author family")
    # email = StringField("author email", validators.Email("Enter Email Address "))
    password =PasswordField("password")
    submit = SubmitField("Submit")