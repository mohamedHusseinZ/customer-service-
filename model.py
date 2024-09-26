#model.py
from db import db  # Import db from the new db module

class Customer(db.Model):
    __tablename__ = 'customer'  # Explicitly define the table name
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    code = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'code': self.code,
            'email': self.email,
            'phone': self.phone,
            'orders': [order.serialize() for order in self.customer_orders]
        }

class Order(db.Model):
    __tablename__ = 'order'  # Explicitly define the table name
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    order_time = db.Column(db.DateTime, default=db.func.current_timestamp())
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    customer = db.relationship('Customer', backref='customer_orders')

    def serialize(self):
        return {
            'id': self.id,
            'item': self.item,
            'amount': str(self.amount),
            'order_time': self.order_time.strftime('%Y-%m-%d %H:%M:%S'),
            'customer_id': self.customer_id
        }
