from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.file import FileAllowed, FileField
from flask_ckeditor import CKEditorField


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    picture = FileField('Add Picture', validators=[FileAllowed(['jpg', 'png'])])
    content = CKEditorField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')
