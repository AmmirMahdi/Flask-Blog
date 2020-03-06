from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,IntegerField,DateTimeField,TextAreaField
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
