from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flasksqlalchemy_ex.config import DebugConfig
import datetime

app = Flask(__name__)

app.config.from_object(DebugConfig)

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    body = db.Column(db.Text, nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)
    category = db.relationship("Category", backref=db.backref("posts", lazy=True))

    def __repr__(self):
        return f"<Post {self.title}>"


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<Category {self.name}>"


"""

db.Integer         an integer

db.String(size)    a string with a maximum length (optional in some databases, e.g. PostgreSQL)

db.Text             some longer unicode text

db.DateTime         date and time expressed as Python datetime object.

db.Float            stores floating point values

db.Boolean          stores a boolean value

db.PickleType       stores a pickled Python object

db.LargeBinary      stores large arbitrary binary data
"""

# One-to-many relationship


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    addresses = db.relationship(
        "Address", backref=db.backref("per", lazy="joined"), lazy=True
    )
    # db.relationship returns a new property
    # that can do multiple things. In this case we
    # told it to point to the Address class and load
    # multiple of those.

    def __repr__(self):
        return f"<Person {self.id} {self.name} {self.addresses}>"


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    person_id = db.Column(
        db.Integer, db.ForeignKey("person.id"), nullable=False
    )  # person.id does not depend on
    # backref but refers to Person
    # model class

    def __repr__(self):
        return f"<Address {self.id} {self.email}>"


"""
* 'select' / True (which is the default, but explicit is better than implicit) means that SQLAlchemy will load the data 
as necessary in one go using a standard select statement.

* 'joined' / False tells SQLAlchemy to load the relationship in the same query as the parent using a JOIN statement.

* 'subquery' works like 'joined' but instead SQLAlchemy will use a subquery.

* 'dynamic' is special and can be useful if you have many items and always want to apply additional SQL filters to them. 
Instead of loading the items SQLAlchemy will return another query object which you can further refine before loading 
the items. Note that this cannot be turned into a different loading strategy when querying so it’s often a good idea 
to avoid using this in favor of lazy=True. A query object equivalent to a dynamic user.addresses relationship can 
be created using Address.query.with_parent(user) while still being able to use lazy or eager loading on the relationship 
itself as necessary.
"""


# Many-to-Many Relationships

tags = db.Table(
    "tags",
    db.Column("tag_id", db.Integer, db.ForeignKey("tag.id"), primary_key=True),
    db.Column("page_id", db.Integer, db.ForeignKey("page.id"), primary_key=True),
)


class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tags = db.relationship(
        "Tag", secondary=tags, lazy="subquery", backref=db.backref("pages", lazy=True)
    )


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)


if __name__ == "__main__":
    try:
        db.drop_all()  # - drop all tables
        db.create_all()  # - create models and database if needed
    except:
        pass

    #  Adding data to the database
    admin = User(username="admin", email="admin@example.com")
    guest = User(username="guest", email="guest@example.com")
    db.session.add(admin)
    db.session.add(guest)
    db.session.commit()

    #  Selecting data from the database
    print(User.query.all())
    print(User.query.filter_by(username="admin").all())  # .first()
    admin = User.query.filter_by(username="admin").first()
    print(admin.id)
    print(admin.username)
    print(admin.email)

    missing = User.query.filter_by(username="missing").first()
    print(missing is None)
    print(User.query.filter(User.email.endswith("@example.com")).all())
    print(User.query.order_by(User.username).all())
    print(User.query.limit(1).all())
    print(User.query.get(1))

    py = Category(name="Python")
    Post(title="Hello Python!", body="Python is pretty cool", category=py)
    p = Post(title="Snakes", body="Shhhhh")
    py.posts.append(p)
    db.session.add(py)
    db.session.commit()

    print(Post.query.all())
    print(Category.query.all())

    from sqlalchemy.orm import joinedload

    query = Category.query.options(joinedload("posts"))
    for category in query:
        print(category, category.posts)
        py = category
        print(Post.query.with_parent(py).filter(Post.title != "Snakes").all())

    print(Person.__tablename__)  # person
    print(Address.__tablename__)  # address
    admin = Person(name="admin")
    Address(email="admin@gmail.com", per=admin)
    Address(email="second_admin@gmail.com", per=admin)
    db.session.add(admin)
    db.session.commit()
    print(Person.query.all())
    print(Address.query.all())

    query = Address.query.options(joinedload("per"))
    for address in query:
        print(address, address.per)
        print(Person.query.with_parent(address).all())
