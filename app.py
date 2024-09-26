#app.py
import os
import requests
from flask import Flask, jsonify, request, redirect
from flask_migrate import Migrate
from config import Config
from db import db  # Import db from the new db module
from flask_oidc import OpenIDConnect
from service import (
    create_customer, get_customer, get_all_customers, update_customer, delete_customer,
    create_order, get_order, get_all_orders, update_order, delete_order
)

# Initialize Flask application
app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions
db.init_app(app)  # Initialize db with the app
migrate = Migrate(app, db)
oidc = OpenIDConnect(app)

# Okta Configurations (ensure env variables are set)
client_secret = os.getenv('KCU9MJMXL0CMI5DJDPI-WJPIPXIIRQLT2E-SNBDOJYEWR_O8LZQKH03OCW4LEM')
client_id = os.getenv('4EUWVOPU94P8KQQGQO0I6V76RQOMCHMG')
issuer = os.getenv('https://dev-soptrf3p4mkmgsza.us.auth0.com')
redirect_uri = os.getenv('REDIRECT_URI', "https://abcd1234.ngrok.io/authorization-code/callback")

@app.route('/profile')
@oidc.require_login
def profile():
    try:
        # Retrieve access token from OIDC session
        access_token = oidc.get_access_token()

        # Make a request to the user info endpoint
        userinfo_url = f"{issuer}/v1/userinfo"
        headers = {'Authorization': f'Bearer {access_token}'}

        response = requests.get(userinfo_url, headers=headers)
        response.raise_for_status()  # Raise an error for bad status codes
        userinfo = response.json()

        return jsonify(userinfo)
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 400

@app.route('/login')
def login():
    # Redirect the user to Okta's authorization URL
    authorization_url = (
        f"{issuer}/v1/authorize?"
        f"client_id={client_id}&response_type=code&scope=openid profile email&redirect_uri={redirect_uri}&state=random_state"
    )
    return redirect(authorization_url)

@app.route('/authorization-code/callback')
def callback():
    # Get the authorization code from the callback
    code = request.args.get('code')

    # Exchange the authorization code for an access token
    token_url = f"{issuer}/v1/token"
    token_data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': redirect_uri,
        'client_id': client_id,
        'client_secret': client_secret
    }
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    # Make the request to exchange the authorization code for tokens
    response = requests.post(token_url, data=token_data, headers=headers)
    token_response = response.json()

    if 'access_token' in token_response:
        return jsonify(token_response)
    else:
        return jsonify({'error': 'Failed to get access token'}), 400

@app.route('/')
def index():
    return 'Welcome to my web!'

# Customer routes
@app.route('/customers', methods=['POST'])
@oidc.require_login
def add_customer():
    try:
        data = request.get_json()
        name = data.get('name')
        code = data.get('code')
        result = create_customer(name, code)
        return jsonify(result), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/customers/<int:customer_id>', methods=['GET'])
@oidc.require_login
def get_customer_route(customer_id):
    try:
        result = get_customer(customer_id)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 404

@app.route('/customers', methods=['GET'])
@oidc.require_login
def get_all_customers_route():
    try:
        result = get_all_customers()
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/customers/<int:customer_id>', methods=['PUT'])
@oidc.require_login
def update_customer_route(customer_id):
    try:
        data = request.get_json()
        name = data.get('name')
        code = data.get('code')
        result = update_customer(customer_id, name, code)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/customers/<int:customer_id>', methods=['DELETE'])
@oidc.require_login
def delete_customer_route(customer_id):
    try:
        result = delete_customer(customer_id)
        return jsonify(result), 204
    except Exception as e:
        return jsonify({'error': str(e)}), 404

# Order routes
@app.route('/orders', methods=['POST'])
@oidc.require_login
def add_order():
    try:
        data = request.get_json()
        item = data.get('item')
        amount = data.get('amount')
        customer_id = data.get('customer_id')
        result = create_order(item, amount, customer_id)
        return jsonify(result), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/orders/<int:order_id>', methods=['GET'])
@oidc.require_login
def get_order_route(order_id):
    try:
        result = get_order(order_id)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 404

@app.route('/orders', methods=['GET'])
@oidc.require_login
def get_all_orders_route():
    try:
        result = get_all_orders()
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/orders/<int:order_id>', methods=['PUT'])
@oidc.require_login
def update_order_route(order_id):
    try:
        data = request.get_json()
        item = data.get('item')
        amount = data.get('amount')
        result = update_order(order_id, item, amount)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/orders/<int:order_id>', methods=['DELETE'])
@oidc.require_login
def delete_order_route(order_id):
    try:
        result = delete_order(order_id)
        return jsonify(result), 204
    except Exception as e:
        return jsonify({'error': str(e)}), 404


if __name__ == '__main__':
    app.run(port=5000, debug=True)
