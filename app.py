from flask import Flask, render_template, redirect, url_for 
import datetime 
import os 
# configurations Database
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate

# Forms 
from forms import PostForm
# config app 
app = Flask(__name__)

# set base directory 
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'blog.sqlite')
app.config['SQL_TRACK_MODIFICATIONS'] = False 
app.config['SECRET_KEY'] = 'amirmahdirashvnad5329@@@@'

db = SQLAlchemy(app)

Migrate(app, db)

# Model 
"""
    Post 
        id 
        title
        author relationship 
        created
        body 
        updated

    Author 
        id
        name 
        family
        email
        password

    Comment 
        
        id
        author
        post
"""


class Author(db.Model):
    
    # set tablename 
    __tablename__= 'author'

    
      
    id        = db.Column(db.Integer, primary_key=True)
    name      = db.Column(db.String, unique=True, nullable=False)
    family    = db.Column(db.String)
    email     = db.Column(db.DateTime)
    password  = db.Column(db.Text)
    user    = db.relationship('User',backref='author',lazy=False)



    def __init__(self, name,family, email, password):
        self.name       = name 
        self.family     = family 
        self.email      = email 
        self.password   = password 

    def report_users(self):

        """
        This function For report users when we need check how many users exist
        """
        users = []
        for i in range(0, 5):
            users.append(self.name)
            users.append(self.family)
            users.append(self.email)
            users.append(self.password)

        for j in users:
            print(j)





class Post(db.Model):

    __tablename__='post'
    
    id          = db.Column(db.Integer, primary_key=True)
    title       = db.Column(db.String, unique=True, nullable=False)
    author      = db.Column(db.String, db.ForeignKey('author.id'))
    created     = db.Column(db.DateTime)
    body        = db.Column(db.Text)
    updated     = db.Column(db.DateTime)
    post        = db.relationship('Comment', backref='post',lazy=True)


    def __init__(self, title, author, created, body, updated):
        self.title       = title 
        self.author      = author 
        self.created     = created 
        self.body        = body 
        self.updated     = updated 

    def __repr__(self):
        return f"object created {self.title}"

class Comment(db.Model):
    __tablename__ = "comment"

    id     = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String, db.ForeignKey('author.id'))
    post   = db.Column(db.String, db.ForeignKey('post.id'))
    body   = db.Column(db.Text)

    def __init__(self, author, post, body):
        self.author = author 
        self.post   = post 
        self.body   = body


@app.route('/add',methods=['GET','POST'])
def add_post():

    form = PostForm()
    """
title   = StringField("post title")
    author  = IntegerField("ID AUTHOR")
    created = DateTimeField('Which date is your favorite?', format='%m/%d/%y', validators=[DataRequired()])
    body    = TextAreaField("Body")
    
    """

    if form.validate_on_submit():
        title = form.title.data 
        author = form.author.data  
        created = form.created.data 
        body    = form.body.data 
        updated = form.updated.data

        new_post = Post(title,author,created,body,updated)
        
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('add.html',form=form)


@app.route('/')
def index():
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True) 
