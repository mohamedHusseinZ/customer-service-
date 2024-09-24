import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://orderly_user:bile@localhost:5432/orderly_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    OIDC_CLIENT_SECRETS = os.getenv('OIDC_CLIENT_SECRETS', 'client_secrets.json')
    OIDC_ISSUER = os.getenv('OKTA_ISSUER', 'https://dev-soptrf3p4mkmgsza.us.auth0.com')
    OIDC_SCOPES = ['openid', 'profile', 'email']
    OKTA_CLIENT_ID = os.getenv('4EUwVOpU94P8kQQGQo0i6V76RQomcHMG')
    OKTA_CLIENT_SECRET = os.getenv('kCU9MjmxL0Cmi5dJDPI-WjpIPXIIRqlT2E-SNBdojYeWr_o8lZQkh03OCwR4lEmg')
    REDIRECT_URI = os.getenv('REDIRECT_URI', 'https://abcd1234.ngrok.io/authorization-code/callback')
    OIDC_PROVIDER_URL = os.getenv('OIDC_PROVIDER_URL', 'https://dev-soptrf3p4mkmgsza.us.auth0.com/oidc')