import json
import unittest
from employees import app, employees

class TestEmployeesAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_employees(self):
        response = self.app.get('/employees')
        data = json.loads(response.data.decode('utf-8'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data, employees)

    def test_get_employee_by_id(self):
        response = self.app.get('/employees/1')
        data = json.loads(response.data.decode('utf-8'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data, employees[0])

    def test_get_nonexistent_employee_by_id(self):
        response = self.app.get('/employees/999')

        self.assertEqual(response.status_code, 404)

    # Add more tests for other routes (POST, PUT, DELETE) following a similar pattern

if __name__ == '__main__':
    unittest.main()
