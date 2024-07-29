import unittest
from unittest.mock import patch
from app import app

class TestEmployees(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_post(self):

        payload = {'id': 1, 'name': 'Sam', 'position': 'admin'}
        response = self.app.post('/employees', json=payload)
        data = response.get_json()
        self.assertEqual(data['result'], 200)


    def test_get(self):

        payload = {'id': 1, 'name': 'Sam', 'position': 'admin'}
        response = self.app.get('/employees', json=payload)
        data = response.get_json()
        self.assertEqual(data['result'], 200)


class TestProduct(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_post(self):

        payload = {'id': 1, 'name': 'laptop', 'price': 30.99}
        response = self.app.post('/products', json=payload)
        data = response.get_json()
        self.assertEqual(data['result'], 200)


    def test_get(self):

        payload = {'id': 1, 'name': 'laptop', 'price': 30.99}
        response = self.app.get('/products', json=payload)
        data = response.get_json()
        self.assertEqual(data['result'], 200)


class TestOrders(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_post(self):

        payload = {'id': 1, 'customer_id': 1, 'product_id': 1, 'quantity': 20, 'total_price': 100}
        response = self.app.post('/orders', json=payload)
        data = response.get_json()
        self.assertEqual(data['result'], 200)


    def test_get(self):

        payload = {'id': 1, 'customer_id': 1, 'product_id': 1, 'quantity': 20, 'total_price': 100}
        response = self.app.get('/orders', json=payload)
        data = response.get_json()
        self.assertEqual(data['result'], 200)


class TestCustomers(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_post(self):

        payload = {'id': 1, 'name': 'Sam', 'email': 'samuelckraft@gmail.com', 'phone': '6154565555'}
        response = self.app.post('/customers', json=payload)
        data = response.get_json()
        self.assertEqual(data['result'], 200)


    def test_get(self):

        payload = {'id': 1, 'name': 'Sam', 'email': 'samuelckraft@gmail.com', 'phone': '6154565555'}
        response = self.app.get('/customers', json=payload)
        data = response.get_json()
        self.assertEqual(data['result'], 200)


class TestProduction(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_post(self):

        payload = {'id': 1, 'product_id': 1, 'quantity_produced': 20, 'date_produced': '2024-01-01'}
        response = self.app.post('/production', json=payload)
        data = response.get_json()
        self.assertEqual(data['result'], 200)


    def test_get(self):

        payload = {'id': 1, 'product_id': 1, 'quantity_produced': 20, 'date_produced': '2024-01-01'}
        response = self.app.get('/production', json=payload)
        data = response.get_json()
        self.assertEqual(data['result'], 200)


if __name__ == '__main__':
    unittest.main()