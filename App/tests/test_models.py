from django.test import TestCase
from App.models import CustomUser, ToDoItems,Tags


class ModelsTestCase(TestCase):

    def test_create_user(self):
        user = CustomUser.objects.create_user(
            username="testuser", password="password")
        self.assertEqual(user.username, "testuser")
        self.assertTrue(user.check_password("password"))

    def test_create_todo_item(self):
        user = CustomUser.objects.create_user(username="testuser", password="password")
        
        self.todo_item = ToDoItems.objects.create(
            user=user,
            title="Test Task",
            description="Description of test task",
            due_date="2024-12-10",
            status="OPEN"
        )
        Tags.objects.bulk_create([
            Tags(tag_name="urgent"),
            Tags(tag_name="work"),
        ])
        tags = Tags.objects.filter(tag_name__in=["urgent", "work"])
        self.todo_item.tags.set(tags)

