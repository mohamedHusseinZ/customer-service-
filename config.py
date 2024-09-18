import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_secret_key')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://orderly_user:yourpassword@localhost:5432/orderly_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    OIDC_CLIENT_SECRETS = os.environ.get('OIDC_CLIENT_SECRETS', 'client_secrets.json')
    OIDC_SCOPES = ['openid', 'profile', 'email']
