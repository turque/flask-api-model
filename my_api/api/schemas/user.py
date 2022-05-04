from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from my_api.extensions import db, ma
from my_api.models import User


class UserSchema(SQLAlchemyAutoSchema):

    id = ma.Int(dump_only=True)
    password = ma.String(load_only=True, required=True)

    class Meta:
        model = User
        sqla_session = db.session
        load_instance = True
        exclude = ("_password", "active")
