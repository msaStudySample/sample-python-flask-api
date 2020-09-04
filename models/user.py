from extentions import db, ma


class User(db.Model):
    email = db.Column(db.VARCHAR(20), primary_key=True)
    password = db.Column(db.VARCHAR(100))
    name = db.Column(db.VARCHAR(50))


class UserSchema(ma.SQLAlchemyAutoSchema):
    email = ma.String()
    password = ma.String()
    name = ma.String()

    class Meta:
        model = User
        sqla_session = db.session
