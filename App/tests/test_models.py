from django.test import TestCase
from App.models import CustomUser, ToDoItems


class ModelsTestCase(TestCase):

    def test_create_user(self):
        user = CustomUser.objects.create_user(
            username="testuser", password="password")
        self.assertEqual(user.username, "testuser")
        self.assertTrue(user.check_password("password"))

    def test_create_todo_item(self):
        user = CustomUser.objects.create_user(
            username="testuser", password="password")
        todo_item = ToDoItems.objects.create(
            user=user,
            title="Test Task",
            description="Description of test task",
            due_date="2024-12-10",
            status="OPEN",
            tags=["urgent", "work"]
        )
        self.assertEqual(todo_item.title, "Test Task")
        self.assertIn("urgent", todo_item.tags)
