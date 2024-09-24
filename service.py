from db import db  # Import db from the new db module
from model import Customer, Order
from sqlalchemy.exc import IntegrityError
import africastalking

# Customer Service Functions
def create_customer(name, code):
    try:
        new_customer = Customer(name=name, code=code)
        db.session.add(new_customer)
        db.session.commit()
        return {"message": "Customer created successfully", "customer": new_customer.serialize()}, 201
    except IntegrityError:
        db.session.rollback()
        return {"message": "Customer code already exists"}, 400

def get_customer(customer_id):
    customer = Customer.query.get(customer_id)
    if customer:
        return customer.serialize()
    else:
        return {"message": "Customer not found"}, 404

def get_all_customers():
    customers = Customer.query.all()
    return [customer.serialize() for customer in customers]

def update_customer(customer_id, name, code):
    customer = Customer.query.get(customer_id)
    if customer:
        customer.name = name
        customer.code = code
        db.session.commit()
        return {"message": "Customer updated successfully", "customer": customer.serialize()}
    else:
        return {"message": "Customer not found"}, 404

def delete_customer(customer_id):
    customer = Customer.query.get(customer_id)
    if customer:
        db.session.delete(customer)
        db.session.commit()
        return {"message": "Customer deleted successfully"}
    else:
        return {"message": "Customer not found"}, 404

# Order Service Functions
def create_order(item, amount, customer_id):
    new_order = Order(item=item, amount=amount, customer_id=customer_id)
    db.session.add(new_order)
    db.session.commit()
    return {"message": "Order created successfully", "order": new_order.serialize()}, 201

def get_order(order_id):
    order = Order.query.get(order_id)
    if order:
        return order.serialize()
    else:
        return {"message": "Order not found"}, 404

def get_all_orders():
    orders = Order.query.all()
    return [order.serialize() for order in orders]

def update_order(order_id, item, amount):
    order = Order.query.get(order_id)
    if order:
        order.item = item
        order.amount = amount
        db.session.commit()
        return {"message": "Order updated successfully", "order": order.serialize()}
    else:
        return {"message": "Order not found"}, 404

def delete_order(order_id):
    order = Order.query.get(order_id)
    if order:
        db.session.delete(order)
        db.session.commit()
        return {"message": "Order deleted successfully"}
    else:
        return {"message": "Order not found"}, 404
