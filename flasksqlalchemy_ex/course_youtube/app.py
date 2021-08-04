from flasksqlalchemy_ex.course_youtube.config import DebugConfig
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime
from faker import Faker
import random

fake = Faker()

app = Flask(__name__)
app.config.from_object(DebugConfig)
db = SQLAlchemy(app)


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(500), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    postcode = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    orders = db.relationship(
        "Order", backref=db.backref("customer", lazy=True), lazy=True
    )
    # Customer().orders =
    # all the orders made by
    # a specific user.

    # Order().customer =
    # a customer who made an
    # order.

    # Order(customer=...) -
    # backref


order_product = db.Table(
    "order_product",
    db.Column("order_id", db.Integer, db.ForeignKey("order.id"), primary_key=True),
    db.Column("product_id", db.Integer, db.ForeignKey("product.id"), primary_key=True),
)


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_date = db.Column(
        db.DateTime, nullable=False, default=datetime.datetime.utcnow
    )
    shipped_date = db.Column(db.DateTime, nullable=True)
    delivery_date = db.Column(db.DateTime, nullable=True)
    coupon_code = db.Column(db.String(50))
    customer_id = db.Column(db.Integer, db.ForeignKey("customer.id"), nullable=False)
    products = db.relationship("Product", secondary=order_product)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    price = db.Column(db.Float, nullable=False)


def create_user():
    johndoe = Customer(
        first_name="John",
        last_name="Doe",
        address="123 Fake Street",
        city="Miami",
        postcode="12-345",
        email="jhondoe@gmail.com",
    )
    db.session.add(johndoe)
    db.session.commit()


def create_product():
    computer = Product(name="Computer", price=80)
    db.session.add(computer)

    phone = Product(name="Phone", price=80)
    db.session.add(phone)
    db.session.commit()


def create_order():
    johndoe = Customer.query.first()
    products = Product.query.all()
    order = Order(coupon_code="FREESHIPPING", customer=johndoe, products=products)

    db.session.add(order)
    db.session.commit()


def update_user():
    johndoe = Customer.query.filter_by(id=1).first()
    print(johndoe.first_name, johndoe.last_name)

    johndoe.address = "456 Fake Street"
    db.session.commit()


def delete_user():
    ashley = Customer(
        first_name="Ashley",
        last_name="Smith",
        address="123 Fake Street",
        city="Miami",
        postcode="12-345",
        email="ashley@gmail.com",
    )

    db.session.add(ashley)
    db.session.commit()
    db.session.delete(ashley)
    db.session.commit()


def add_customers():
    for _ in range(100):
        customer = Customer(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            address=fake.street_address(),
            city=fake.city(),
            postcode=fake.postcode(),
            email=fake.email(),
        )
        db.session.add(customer)
    db.session.commit()


def add_orders():
    customers = Customer.query.all()

    for _ in range(1000):
        customer = random.choice(customers)

        ordered_date = fake.date_time_this_year()
        shipped_date = random.choices(
            [None, fake.date_time_between(start_date=ordered_date)], [10, 90]
        )[0]

        delivered_date = None
        if shipped_date:
            delivered_date = random.choices(
                [None, fake.date_time_between(start_date=shipped_date)], [50, 50]
            )[0]
            # random.choices(sequence, weights=None, cum_weights=None, k=1)
        coupon_code = random.choices(
            [None, "FREESHIPPING", "50OFF", "BUYONEGETONE"], [80, 5, 5, 5]
        )[0]

        order = Order(
            customer=customer,
            order_date=ordered_date,
            delivery_date=delivered_date,
            shipped_date=shipped_date,
            coupon_code=coupon_code,
        )

        db.session.add(customer)
    db.session.commit()


def add_products():
    for _ in range(10):
        product = Product(name=fake.color_name(), price=random.randint(10, 100))
        db.session.add(product)
    db.session.commit()


def add_order_products():
    orders = Order.query.all()
    products = Product.query.all()

    for order in orders:
        k = random.randint(1, 3)
        purchased_products = random.sample(products, k)  # select k random products
        order.products.extend(purchased_products)

    db.session.commit()


def get_orders_by(customer_id=1):
    customer_orders = Order.query.filter_by(customer_id=customer_id).all()
    for order in customer_orders:
        print(order.id, order.customer, order.order_date)


def get_pending_orders():
    print("Pending Orders: ")
    pending_orders = (
        Order.query.filter(Order.shipped_date.is_(None))
        .order_by(Order.order_date.desc())
        .all()
    )
    for order in pending_orders:
        print(order.order_date)


def get_customer_count():
    print("How many customers: ")
    print(Customer.query.count())


def orders_with_code():
    print("Orders with coupon code: ")
    for order in (
        Order.query.filter(Order.coupon_code.isnot(None))
        .filter(Order.coupon_code != "FREESHIPPING")
        .all()
    ):
        print(order.coupon_code)


def revenue_in_last_x_days(x_days=30):
    print("Revenue in past x days: ")
    data = (
        db.session.query(db.func.sum(Product.price))
        .join(order_product)
        .join(Order)
        .filter(
            Order.order_date
            > (datetime.datetime.now() - datetime.timedelta(days=x_days))
        )
        .scalar()
    )
    print(data)


def average_fulfillment_time():
    print("Average fulfillment time: ")
    print(
        db.session.query(
            db.func.time(
                db.func.avg(
                    db.func.strftime("%s", Order.shipped_date)
                    - db.func.strftime(Order.order_date)
                ),
                "unixepoch",
            )
        )
        .filter(Order.shipped_date.isnot(None))
        .scalar()
    )


def get_customers_purchased_x_values(x=500):
    print("All customers who have purchased x values")
    data = (
        db.session.query(Customer)
        .join(Order)
        .join(order_product)
        .join(Product)
        .group_by(Customer)
        .having(db.func.sum(Product.price) > x)
        .all()
    )
    for customer in data:
        print(customer.first_name)


if __name__ == "__main__":
    try:
        db.drop_all()
    except:
        pass

    try:
        db.create_all()
    except:
        pass

    # create_user()
    # create_product()
    # create_order()
    # update_user()
    # delete_user()

    add_customers()
    add_orders()
    add_products()
    add_order_products()

    get_orders_by()
    get_pending_orders()
    get_customer_count()
    orders_with_code()
    revenue_in_last_x_days()
    average_fulfillment_time()
    get_customers_purchased_x_values()
