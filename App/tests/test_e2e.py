from rest_framework.test import APIClient
from django.test import TestCase
from App.models import CustomUser,ToDoItems


class E2ETest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(
            username="testuser", password="password")
        self.client.force_authenticate(user=self.user)

    def test_create_todo_item(self):

        # creating a to-do item
        response = self.client.post(
            '/items/',
            {
                "title": "Test Task",
                "description": "Description of test task",
                "due_date": "2024-12-10",
                "status": "OPEN",
                "tags": ["urgent", "work"]
            },
            format='json'
        )
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.data['data'])

        #query the db
        item = ToDoItems.objects.get(id=response.data['data']['id'])
        self.assertIsNotNone(item)

    def test_view_all_todo_items(self):
        # creating a to-do item
        response = self.client.post(
            '/items/',
            {
                "title": "Test Task",
                "description": "Description of test task",
                "due_date": "2024-12-10",
                "status": "OPEN",
                "tags": ["urgent", "work"]
            },
            format='json'
        )
        self.assertEqual(response.status_code, 201)
        # getting all to-do items
        response = self.client.get('/items/')
        self.assertEqual(response.status_code, 200)

        # query the db 
        items = ToDoItems.objects.all()
        self.assertEqual(len(response.data), items.count())

    def test_update_todo_item(self):
        # first creating a to-do item
        response = self.client.post(
            '/items/',
            {
                "title": "Test Task",
                "description": "Description of test task",
                "due_date": "2024-12-10",
                "status": "OPEN",
                "tags": ["urgent", "work"]
            },
            format='json'
        )
        self.assertEqual(response.status_code, 201)
        item_id = response.data['data']['id']


        # updating the to-do item
        response = self.client.put(
            f'/items/{item_id}/',
            {
                "title": "Updated Task",
                "description": "Updated description",
                "due_date": "2024-12-10",
                "status": "OPEN",
                "tags": ["urgent", "work"]
            },
            format='json'
        )
        self.assertEqual(response.status_code, 202)

        #query the db
        item = ToDoItems.objects.get(id=item_id)
        self.assertEqual(item.title, "Updated Task")

    def test_delete_todo_item(self):
        # first creating a to-do item
        response = self.client.post(
            '/items/',
            {
                "title": "Test Task",
                "description": "Description of test task",
                "due_date": "2024-12-10",
                "status": "OPEN",
                "tags": ["urgent", "work"]
            },
            format='json'
        )
        self.assertEqual(response.status_code, 201)
        item_id = response.data['data']['id']

        # deleting the to-do item
        response = self.client.delete(f'/items/{item_id}/')
        self.assertEqual(response.status_code, 204)

        #query the db
        item = ToDoItems.objects.filter(id=item_id)
        self.assertFalse(item.exists())

        # checking if deleted
        response = self.client.get(f'/items/{item_id}/')
        self.assertEqual(response.status_code, 404)
