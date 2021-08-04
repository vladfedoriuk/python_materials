from flask import Flask, jsonify, request, flash, render_template
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

dir_name = os.path.abspath(os.path.dirname(__file__))
db_uri = "sqlite:///" + os.path.abspath(os.path.join(dir_name, "flasksql_2.db"))

app.config.update(
    DEBUG=True,
    SECRET_KEY="secret",
    WTF_CSRF_ENABLED=False,
    SQLALCHEMY_DATABASE_URI=db_uri,
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)

db = SQLAlchemy(app)


@app.route("/posts/", methods=["GET", "POST"])
def posts():
    from flasksqlalchemy_ex.tceh.models import User, Post
    from flasksqlalchemy_ex.tceh.forms import UserForm, PostForm

    if request.method == "POST":
        print(request.form)
        form = PostForm(request.form)
        if form.validate():
            post = Post(**form.data)
            db.session.add(post)
            db.session.commit()
            flash("Post created")
        else:
            flash("Post was not created")
            flash(form.errors)

    all_posts = Post.query.all()
    for post in all_posts:
        print(post.user, post)

    return render_template("home.txt", posts=all_posts)


if __name__ == "__main__":
    from flasksqlalchemy_ex.tceh.models import *
    from flasksqlalchemy_ex.tceh.models import User

    # db.create_all()

    # user = User(username='vladfedoriuk', email='vladfedoriuk@gmail.com')
    # db.session.add(user)
    # db.session.commit()
    app.run()
