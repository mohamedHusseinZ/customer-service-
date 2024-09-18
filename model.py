from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    code = db.Column(db.String(50), unique=True, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'code': self.code,
            'orders': [order.serialize() for order in self.orders]
        }

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    order_time = db.Column(db.DateTime, default=db.func.current_timestamp())
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    customer = db.relationship('Customer', backref='orders')

    def serialize(self):
        return {
            'id': self.id,
            'item': self.item,
            'amount': str(self.amount),
            'order_time': self.order_time.strftime('%Y-%m-%d %H:%M:%S'),
            'customer_id': self.customer_id
        }
