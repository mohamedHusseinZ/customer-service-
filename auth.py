from flask_oidc import OpenIDConnect
from flask import redirect, url_for, session
from functools import wraps
import os

# Initialize OpenIDConnect
oidc = OpenIDConnect()

def requires_auth(f):
    """Decorator to check if the user is authenticated"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not oidc.user_loggedin:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def login():
    """Login route that initiates the OpenID Connect flow"""
    if oidc.user_loggedin:
        return redirect(url_for('index'))
    return oidc.redirect_to_auth_server(request.url)

def logout():
    """Logout route to clear session and redirect to logout endpoint"""
    session.clear()
    return redirect(url_for('index'))

def handle_oidc_error():
    """Handle errors from OpenID Connect"""
    return {"message": "Authentication failed"}, 401

def initialize_oidc(app):
    """Initialize OpenID Connect with the Flask app"""
    app.config['OIDC_CLIENT_SECRETS'] = 'client_secrets.json'
    app.config['OIDC_SCOPES'] = ['openid', 'profile', 'email']
    app.config['OIDC_OPENID_REALM'] = 'orderly'
    app.config['OIDC_ID_TOKEN_COOKIE_SECURE'] = False  # Set to True in production
    oidc.init_app(app)

# Route example for testing authentication
@app.route('/private')
@requires_auth
def private():
    return 'This is a private page!'

