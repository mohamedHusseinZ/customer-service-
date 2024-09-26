from app import create_app
import unittest

class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_customer(self):
        response = self.client.post('/customers', json={
            "name": "John Doe",
            "email": "john@example.com"
        })
        self.assertEqual(response.status_code, 201)

    def test_create_order(self):
        response = self.client.post('/orders', json={
            "customer_id": 1,
            "product": "Laptop",
            "quantity": 2
        })
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()
