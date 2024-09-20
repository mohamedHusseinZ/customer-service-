#service.py
from model import db, Customer, Order
from sqlalchemy.exc import IntegrityError
import africastalking

# Initialize Africa's Talking
def initialize_africastalking():
    africastalking.initialize(username='your_username', api_key='your_api_key')

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
        return customer.serialize(), 200
    return {"message": "Customer not found"}, 404

def get_all_customers():
    customers = Customer.query.all()
    return [customer.serialize() for customer in customers], 200

def update_customer(customer_id, name=None, code=None):
    customer = Customer.query.get(customer_id)
    if not customer:
        return {"message": "Customer not found"}, 404
    
    if name:
        customer.name = name
    if code:
        customer.code = code

    try:
        db.session.commit()
        return {"message": "Customer updated successfully", "customer": customer.serialize()}, 200
    except IntegrityError:
        db.session.rollback()
        return {"message": "Customer code already exists"}, 400

def delete_customer(customer_id):
    customer = Customer.query.get(customer_id)
    if not customer:
        return {"message": "Customer not found"}, 404

    db.session.delete(customer)
    db.session.commit()
    return {"message": "Customer deleted successfully"}, 200

# Order Service Functions

def create_order(item, amount, customer_id):
    customer = Customer.query.get(customer_id)
    if not customer:
        return {"message": "Customer not found"}, 404
    
    new_order = Order(item=item, amount=amount, customer_id=customer.id)
    db.session.add(new_order)
    db.session.commit()

    # Send SMS to customer
    message = f"Order received: {item} for {amount} units."
    send_sms(customer.code, message)
    
    return {"message": "Order created successfully", "order": new_order.serialize()}, 201

def get_order(order_id):
    order = Order.query.get(order_id)
    if order:
        return order.serialize(), 200
    return {"message": "Order not found"}, 404

def get_all_orders():
    orders = Order.query.all()
    return [order.serialize() for order in orders], 200

def update_order(order_id, item=None, amount=None):
    order = Order.query.get(order_id)
    if not order:
        return {"message": "Order not found"}, 404
    
    if item:
        order.item = item
    if amount:
        order.amount = amount

    db.session.commit()
    return {"message": "Order updated successfully", "order": order.serialize()}, 200

def delete_order(order_id):
    order = Order.query.get(order_id)
    if not order:
        return {"message": "Order not found"}, 404

    db.session.delete(order)
    db.session.commit()
    return {"message": "Order deleted successfully"}, 200

def send_sms(phone_number, message):
    """Send an SMS using Africa's Talking."""
    try:
        africastalking.SMS.send(message, phone_number)
    except Exception as e:
        raise RuntimeError(f"Failed to send SMS: {e}")

# Initialize Africa's Talking configuration (run this at startup or in your main function)
initialize_africastalking()
