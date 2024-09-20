import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_secret_key')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://orderly_user:bile@localhost:5432/orderly_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    OIDC_CLIENT_SECRETS = os.environ.get('OIDC_CLIENT_SECRETS', 'client_secrets.json')
    OIDC_ISSUER = os.environ.get('OIDC_ISSUER', 'https://accounts.google.com')  # Set a default or ensure it's set in the .env file
    OIDC_SCOPES = ['openid', 'profile', 'email']
    OIDC_PROVIDER_URL = os.environ.get('OIDC_PROVIDER_URL', 'https://accounts.google.com/.well-known/openid-configuration')  # Ensure this is correctly set
