import unittest
from fastapi.testclient import TestClient
from app.main import app, Msg


class TestAPI(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(app)

    def test_root(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Hello World. Welcome to the API home page!"})

    def test_function_demo_get(self):
        response = self.client.get("/path")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "This is /path endpoint, use post request to transform text to uppercase"})

    def test_function_demo_post(self):
        input_data = {"msg": "hello"}
        response = self.client.post("/path", json=input_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "HELLO"})

    def test_function_demo_get_path_id(self):
        path_id = 123
        response = self.client.get(f"/path/{path_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": f"This is /path/{path_id} endpoint, use post request to retrieve result"})


if __name__ == '__main__':
    unittest.main()