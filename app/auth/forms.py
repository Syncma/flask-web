from wtforms import Form, StringField, PasswordField
from wtforms.validators import ValidationError, DataRequired, Length, Email


class LoginForm(Form):
    username = StringField(validators=[DataRequired(), Length(min=1, max=5)])
    password = PasswordField(validators=[DataRequired(), Length(min=1, max=5)])
    email = StringField(validators=[
        DataRequired(),
        Email(),
        Length(min=1, max=10, message="参数必须是1-10")
    ])
