import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    # Flask and database configuration
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_secret_key')
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL', 'postgresql://orderly_user:bile@localhost:5432/orderly_db'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # OpenID Connect (OIDC) Configuration
    OIDC_CLIENT_SECRETS = os.environ.get('OIDC_CLIENT_SECRETS', 'client_secrets.json')
    OIDC_ISSUER = os.environ.get('OKTA_ISSUER', 'https://dev-soptrf3p4mkmgsza.us.auth0.com')
    OIDC_SCOPES = ['openid', 'profile', 'email']

    # Okta-specific Configuration
    OKTA_CLIENT_ID = os.environ.get('OKTA_CLIENT_ID')
    OKTA_CLIENT_SECRET = os.environ.get('OKTA_CLIENT_SECRET')
    REDIRECT_URI = os.environ.get('REDIRECT_URI', 'http://127.0.0.1:5000/authorization-code/callback')

    # OIDC Provider URL
    OIDC_PROVIDER_URL = os.environ.get(
        'OIDC_PROVIDER_URL', 'https://dev-soptrf3p4mkmgsza.us.auth0.com/oidc'
    )
