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

    def test_register_user(self):
        response = self.client.post(
            '/register/', {"name": "test user", "email": "test@email.com", "username": "newuser", "password": "password"})
        self.assertEqual(response.status_code, 201)

    def test_login_user(self):
        response = self.client.post(
            '/login/', {"username": "testuser", "password": "password"})
        self.assertEqual(response.status_code, 200)

    def test_get_all_todo_items(self):
        response = self.client.get('/items/')
        self.assertEqual(response.status_code, 200)

    def test_create_todo_item(self):
        response = self.client.post('/items/', {
            "title": "New Task",
            "description": "New description",
            "due_date": "2024-12-15",
            "status": "OPEN",
            "tags": ["home", "urgent"]
        }, format='json')
        self.assertEqual(response.status_code, 201)

    def test_update_todo_item(self):
        response = self.client.put(f'/items/{self.todo_item.id}/', {
            "title": "Updated Task",
            "description": "Updated description",
            "due_date": "2024-12-20",
            "status": "COMPLETED",
            "tags": ["home", "updated"]
        }, format='json')
        self.assertEqual(response.status_code, 202)

    def test_delete_todo_item(self):
        response = self.client.delete(f'/items/{self.todo_item.id}/')
        self.assertEqual(response.status_code, 204)
