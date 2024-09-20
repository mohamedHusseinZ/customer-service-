from sqlalchemy import inspect
from datetime import datetime
from app import app, db
from model import Customer, Order
from sqlalchemy.exc import SQLAlchemyError

def seed_database():
    with app.app_context():
        # Create all tables
        db.create_all()
        
        # Inspect the database for tables
        inspector = inspect(db.engine)
        tables = inspector.get_table_names()
        
        # Check if the 'customer' table exists
        if 'customer' in tables:
            print("Table 'customer' exists.")
        else:
            print("Table 'customer' does not exist.")
            return  # Exit if the table does not exist

        # Sample data
        customers = [
            Customer(name='John Doe', code='CUST001'),
            Customer(name='Jane Smith', code='CUST002')
        ]
        
        orders = [
            Order(item='Laptop', amount=999.99, order_time=datetime(2024, 9, 19, 10, 0, 0), customer_id=1),
            Order(item='Mouse', amount=25.50, order_time=datetime(2024, 9, 19, 11, 0, 0), customer_id=2)
        ]

        try:
            # Add sample data to the session
            db.session.bulk_save_objects(customers)
            db.session.bulk_save_objects(orders)
            db.session.commit()
            print("Data seeded successfully.")
        except SQLAlchemyError as e:
            db.session.rollback()
            print(f"An error occurred: {e}")

if __name__ == '__main__':
    seed_database()
