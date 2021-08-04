from flasksqlalchemy_ex.tceh.flasksql_2 import db
from datetime import date


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(70), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    posts = db.relationship("Post", backref=db.backref("user", lazy=True), lazy=True)

    def __repr__(self):
        return f"<User {self.username}>"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey("user.id"), nullable=False, index=True
    )
    title = db.Column(db.String(120), unique=True, nullable=False)
    content = db.Column(db.String(3000), nullable=False)
    date_created = db.Column(db.Date, default=date.today)
    is_visible = db.Column(db.Boolean, default=True, nullable=False)

    def __repr__(self):
        return f"<Post {self.id} of User {self.user_id}>"
