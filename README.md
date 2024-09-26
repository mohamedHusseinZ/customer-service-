# customer-service-

Customer Service Management System
Overview
This project is a Customer Service Management System developed using Flask, PostgreSQL, and Docker. It provides RESTful APIs to manage customers and orders, along with JWT authentication and OIDC for secure access. The application is designed to facilitate easy management of customer data and orders, suitable for retail and wholesale businesses.

Table of Contents
Features
Technologies
Setup
Running the Application
Docker
Deployment
Endpoints
Testing
Contributing
License
Features
Customer Management: Add, update, retrieve, and delete customer information.
Order Management: Create, update, retrieve, and delete orders associated with customers.
JWT Authentication: Secure access to the APIs using JSON Web Tokens.
OIDC Integration: Authentication using OpenID Connect.
Persistent Storage: Data is stored in a PostgreSQL database.
Docker Support: Easy deployment and management using Docker containers.
Technologies
Programming Language: Python 3.11
Framework: Flask
Database: PostgreSQL 14
Containerization: Docker
Deployment Platform: Render (for production)
Testing: pytest
Setup
Prerequisites
Python 3.11
PostgreSQL
Docker and Docker Compose

Installation
Clone the repository:
git clone https://github.com/mohamedHusseinZ/customer-service.git
cd customer-service

Create a virtual environment and activate it:
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install dependencies:
pip install -r requirements.txt

Set up the PostgreSQL database:

Ensure PostgreSQL is running and create a database named orderly_db with the user orderly_user and password bile

Running the Application
To run the Flask application using the built-in development server, execute the following command:

You should see output similar to the following:
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
You can now access the application at http://127.0.0.1:5000. The following endpoints are available:

GET /customers: Retrieve all customers.
GET /orders: Retrieve all orders.


Docker
Build and Run
Build the Docker image:

docker-compose build

Start the application:
docker-compose up

Accessing the Application
The application will be accessible at http://127.0.0.1:5000

Deployment
The application is deployed on Render. The Docker images are built and deployed automatically, and the following environment variables are configured:

DATABASE_URL: Connection string for PostgreSQL.
OIDC_CLIENT_SECRETS: Path to OIDC client secrets JSON file.
Deployment Links

https://customer-service-4.onrender.com

Orders API: https://customer-service-4.onrender.com/orders
Customers API: https://customer-service-4.onrender.com/customers


Kubernetes Deployment
For deployment on Kubernetes, the following YAML files are provided:

flask-deployment.yml: Configures the Flask application deployment and service.
postgres-deployment.yml: Configures the PostgreSQL deployment and service with persistent storage.


Endpoints
Customers
GET /customers: Retrieve all customers.
POST /customers: Add a new customer.
GET /customers/<id>: Retrieve a specific customer by ID.
PUT /customers/<id>: Update a specific customer by ID.
DELETE /customers/<id>: Delete a specific customer by ID.
Orders
GET /orders: Retrieve all orders.
POST /orders: Add a new order.
GET /orders/<id>: Retrieve a specific order by ID.
PUT /orders/<id>: Update a specific order by ID.
DELETE /orders/<id>: Delete a specific order by ID.


Testing
pytest --cov

Conclusion
This project showcases my skills in developing RESTful APIs, containerization with Docker, and orchestration with Kubernetes. It demonstrates my ability to build scalable and maintainable applications, which I believe will be valuable in a technical role.



