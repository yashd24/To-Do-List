from django.test import TestCase
from rest_framework.test import APIClient
from App.models import CustomUser, ToDoItems


class ViewsTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(
            username="testuser", password="password")
        self.todo_item = ToDoItems.objects.create(
            user=self.user,
            title="Test Task",
            description="Description of test task",
            due_date="2024-12-10",
            status="OPEN",
            tags=["urgent", "work"]
        )
        self.client.force_authenticate(user=self.user)

    # register user
    def test_register_user(self):
        response = self.client.post(
            '/register/',
            {
                "name": "test user",
                "email": "test@email.com",
                "username": "newuser",
                "password": "password"
            }
        )
        self.assertEqual(response.status_code, 201)

    def test_invalid_register(self):
        response = self.client.post(
            '/register/',
            {
                "name": "test user",
                "email": "test@email.com",
                "password": "password"
            }
        )
        self.assertEqual(response.status_code, 400)

    # login user
    def test_login_user(self):
        response = self.client.post(
            '/login/',
            {
                "username": "testuser",
                "password": "password"
            }
        )
        self.assertEqual(response.status_code, 200)

    # get all todo items
    def test_get_all_todo_items(self):
        response = self.client.get('/items/')
        self.assertEqual(response.status_code, 200)

    # get todo item by id
    def test_get_todo_item_by_id(self):
        response = self.client.get(f'/items/{self.todo_item.id}/')
        self.assertEqual(response.status_code, 200)

    # create todo item
    def test_create_todo_item(self):
        response = self.client.post(
            '/items/',
            {
                "title": "New Task",
                "description": "New description",
                "due_date": "2024-12-15",
                "status": "OPEN",
                "tags": ["home", "urgent"]
            },
            format='json'
        )
        self.assertEqual(response.status_code, 201)

    # update todo item
    def test_update_todo_item(self):
        response = self.client.put(
            f'/items/{self.todo_item.id}/',
            {
                "title": "Updated Task",
                "description": "Updated description",
                "due_date": "2024-12-20",
                "status": "COMPLETED",
                "tags": ["home", "updated"]
            },
            format='json'
        )
        self.assertEqual(response.status_code, 202)

    # delete todo item
    def test_delete_todo_item(self):
        response = self.client.delete(f'/items/{self.todo_item.id}/')
        self.assertEqual(response.status_code, 204)

    # Login with incorrect password

    def test_login_invalid_password(self):
        response = self.client.post(
            '/login/',
            {"username": "testuser", "password": "wrongpassword"}
        )
        self.assertEqual(response.status_code, 401)

    # Login with non-existent user

    def test_login_nonexistent_user(self):
        response = self.client.post(
            '/login/',
            {"username": "nonexistent", "password": "password"}
        )
        self.assertEqual(response.status_code, 404)

    # Get ToDo items when no items exist

    def test_get_no_todo_items(self):
        self.todo_item.delete()  # Ensure no items exist for the user
        response = self.client.get('/items/')
        self.assertEqual(response.status_code, 404)

    # Create ToDo item with invalid data

    def test_create_todo_item_invalid_data(self):
        response = self.client.post(
            '/items/',
            # Missing required fields
            {"title": "", "description": "Invalid description"},
            format='json'
        )
        self.assertEqual(response.status_code, 400)

    # Update ToDo item with invalid data

    def test_update_todo_item_invalid_data(self):
        response = self.client.put(
            f'/items/{self.todo_item.id}/',
            # Missing required fields
            {"title": "", "description": "Invalid description"},
            format='json'
        )
        self.assertEqual(response.status_code, 400)

    # tag validation
    def test_tag_validation(self):
        response = self.client.post(
            '/items/',
            {
                "title": "New Task",
                "description": "New description",
                "due_date": "2024-12-15",
                "status": "OPEN",
                "tags": "home"
            },
            format='json'
        )
        self.assertEqual(response.status_code, 400)
