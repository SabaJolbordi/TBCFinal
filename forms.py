
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed, FileSize
from wtforms.fields import StringField, SubmitField

from wtforms import StringField, IntegerField, SubmitField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, length, equal_to
from wtforms.validators import DataRequired, Length

# class MyForm(FlaskForm):
#     text_field = StringField('Enter Text', validators=[DataRequired()])
#     submit_button = SubmitField('Submit')
class AddProductForm(FlaskForm):
    maintitle = StringField("The title of the activity", validators=[DataRequired()])
    img = FileField("The name of img",
                    validators=[
                        FileRequired(),
                        FileAllowed(["jpeg", "jpg", "png"], message="Only pictures are acceptable"),
                        FileSize(1024 * 1024 * 5, message="The file must be a maximum of 5 megabytes")
                    ])
    card_title = StringField(" The card text", validators=[DataRequired()])
    time = StringField("Activity time", validators=[DataRequired()])
    submit = SubmitField("Add")



# class EditProductForm(FlaskForm):
#         maintitle = StringField('Maintitle', validators=[DataRequired()])
#         img = FileField('Image',
#                         validators=[
#                             FileRequired(),
#                             FileAllowed(["jpeg", "jpg", "png"], message="Only pictures are acceptable"),
#                             FileSize(1024 * 1024 * 5, message="The file must be a maximum of 5 megabytes")
#                         ])
#         card_title = StringField(" The card text", validators=[DataRequired()])
#         time = StringField("Activity time", validators=[DataRequired()])
#         submit = SubmitField("Edit")

class EditProductForm(FlaskForm):
    maintitle = StringField('Maintitle', validators=[DataRequired(), Length(max=255)])
    img = FileField('Image', validators=[FileAllowed(["jpeg", "jpg", "png"], message="Only pictures are acceptable")])
    card_title = StringField('Card Title', validators=[DataRequired(), Length(max=255)])
    time = StringField('Time', validators=[DataRequired(), Length(max=255)])
    submit = SubmitField('Save Changes')


    # class EditProductForm(FlaskForm):
    #     maintitle = StringField("The title of the activity", validators=[DataRequired()])
    #     img = FileField("The name of img",
    #                     validators=[
    #                         FileRequired(),
    #                         FileAllowed(["jpeg", "jpg", "png"], message="Only pictures are acceptable"),
    #                         FileSize(1024 * 1024 * 5, message="The file must be a maximum of 5 megabytes")
    #                     ])
    #     card_title = StringField(" The card text", validators=[DataRequired()])
    #     time = StringField("Activity time", validators=[DataRequired()])
    #     submit = SubmitField("Add")




class RegisterForm(FlaskForm):
    username = StringField("Enter username")
    password = PasswordField("Enter the password",validators=[length(min=6, max=64, message= "Password must be longer than 8 characters")])
    repeat_password = PasswordField("repeat password", validators=[equal_to("password", message="Passwords do not match")])
    submit = SubmitField("Registration")



class LoginForm(FlaskForm):
    username = StringField("Enter username", validators=[DataRequired()])
    password = PasswordField("Enter the password", validators=[DataRequired()])

    submit = SubmitField("Authorization")
