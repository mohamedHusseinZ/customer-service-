import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from model import Customer, Order, db  # Ensure the models are imported correctly

# Set up your database connection
DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://orderly_user:bile@localhost:5432/orderly_db')
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def create_tables():
    """Create the database tables based on the models."""
    db.metadata.create_all(engine)

def seed_data():
    session = Session()

    # Sample customer data
    customers = [
        Customer(name='John Doe', code='C001', email='john@example.com', phone='1234567890'),
        Customer(name='Jane Smith', code='C002', email='jane@example.com', phone='0987654321'),
    ]

    # Sample order data
    orders = [
        Order(item='Product A', amount=99.99, customer_id=1),
        Order(item='Product B', amount=49.99, customer_id=2),
    ]

    try:
        # Add customers to the session
        session.add_all(customers)
        session.commit()  # Commit the transaction
        print("Customer data seeded successfully.")

        # Add orders to the session
        session.add_all(orders)
        session.commit()  # Commit the transaction
        print("Order data seeded successfully.")

    except IntegrityError as e:
        session.rollback()  # Roll back in case of error
        print(f"Error occurred: {str(e)}")

    finally:
        session.close()  # Close the session

if __name__ == "__main__":
    create_tables()
    seed_data()
