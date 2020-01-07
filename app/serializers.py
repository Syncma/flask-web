from app import ma
from app.models import User


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User


user_schema = UserSchema()