from flask import Flask, request, jsonify
from model import db
from service import create_customer, get_customer, get_all_customers, update_customer, delete_customer
from service import create_order, get_order, get_all_orders, update_order, delete_order
from auth import oidc

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://orderly_user:yourpassword@localhost:5432/orderly_db'

db.init_app(app)


# Secure routes using OpenID Connect
@app.route('/secure/customers', methods=['GET'])
@oidc.require_login
def secure_customers():
    return get_all_customers()

# Customer Routes
@app.route('/customers', methods=['POST'])
def add_customer():
    data = request.json
    return create_customer(data['name'], data['code'])

@app.route('/customers/<int:customer_id>', methods=['GET'])
def get_customer_by_id(customer_id):
    return get_customer(customer_id)

@app.route('/customers', methods=['GET'])
def get_all_customers_route():
    return get_all_customers()

@app.route('/customers/<int:customer_id>', methods=['PUT'])
def update_customer_route(customer_id):
    data = request.json
    return update_customer(customer_id, data.get('name'), data.get('code'))

@app.route('/customers/<int:customer_id>', methods=['DELETE'])
def delete_customer_route(customer_id):
    return delete_customer(customer_id)

# Order Routes
@app.route('/orders', methods=['POST'])
def add_order():
    data = request.json
    return create_order(data['item'], data['amount'], data['customer_id'])

@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order_by_id(order_id):
    return get_order(order_id)

@app.route('/orders', methods=['GET'])
def get_all_orders_route():
    return get_all_orders()

@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order_route(order_id):
    data = request.json
    return update_order(order_id, data.get('item'), data.get('amount'))

@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order_route(order_id):
    return delete_order(order_id)

if __name__ == '__main__':
    app.run(debug=True)
