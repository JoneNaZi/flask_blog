from run import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(36))
    password = db.Column(db.String(36))


# db.create_all()
