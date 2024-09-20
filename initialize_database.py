from app import app, db
from model import Customer, Order

def initialize_database():
    with app.app_context():
        # Create all tables
        db.create_all()
        print("Tables created successfully.")

if __name__ == '__main__':
    initialize_database()
