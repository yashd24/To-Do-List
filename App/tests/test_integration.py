from django.test import TestCase
from rest_framework.test import APIClient
from App.models import CustomUser, ToDoItems


class IntegrationTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    # register and login user
    def register_and_login_user(self):

        invalid_register_response = self.client.post(
            '/register/',
            {
                "name": "test user",
                "email": "test@email.com",
                "password": "password"
            }
        )
        self.assertEqual(invalid_register_response.status_code, 400)

        # user not found
        user_not_found_response = self.client.post(
            '/login/',
            {
                "username": "newuser",
                "password": "password"
            }
        )
        self.assertEqual(user_not_found_response.status_code, 404)

        # register new user
        register_response = self.client.post(
            '/register/',
            {
                "name": "test user",
                "email": "test@email.com",
                "username": "newuser",
                "password": "password"
            }
        )
        self.assertEqual(register_response.status_code, 201)

        # invalid login creds
        invalid_login_response = self.client.post(
            '/login/',
            {
                "username": "newuser",
                "password": "wrongpassword"
            }
        )
        self.assertEqual(invalid_login_response.status_code, 401)

        # login user
        login_response = self.client.post(
            '/login/',
            {
                "username": "newuser",
                "password": "password"
            }
        )
        self.assertEqual(login_response.status_code, 200)
        self.assertIn('access', login_response.data)
        self.assertIn('refresh', login_response.data)

        self.access_token = login_response.data['access']

    def authenticate(self):
        login_response = self.client.post(
            '/login/',
            {
                "username": "newuser",
                "password": "password"
            }
        )

        token = login_response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    def test_create_todo_items(self):
        self.register_and_login_user()
        self.authenticate()

        # items not found
        get_response = self.client.get('/items/')
        self.assertEqual(get_response.status_code, 404)

        # invalid create request
        invalid_create_response = self.client.post(
            '/items/',
            {
                "title": "New Task",
                "due_date": "2024-12-15",
                "status": "OPEN",
                "tags": ["home", "urgent"]
            },
            format='json'
        )
        self.assertEqual(invalid_create_response.status_code, 400)

        # invalid tag
        tag_validation_response = self.client.post(
            '/items/',
            {
                "title": "New Task",
                "description": "New description",
                "due_date": "2024-12-15",
                "status": "OPEN",
                "tags": "home",
            },
            format='json'
        )
        self.assertEqual(tag_validation_response.status_code, 400)

        # create a new item
        create_response = self.client.post(
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
        self.assertEqual(create_response.status_code, 201)
        item_id = create_response.data['data']['id']

        # get all items
        get_response = self.client.get('/items/')
        self.assertEqual(get_response.status_code, 200)

        # get the item
        get_item_response = self.client.get(f'/items/{item_id}/')
        self.assertEqual(get_item_response.status_code, 200)

        invalid_update_response = self.client.put(
            f'/items/{item_id}/',
            {
                "title": "Updated Task",
                "due_date": "2024-12-20",
                "status": "COMPLETED",
                "tags": ["home", "updated"]
            },
            format='json'
        )
        self.assertEqual(invalid_update_response.status_code, 404)

        # update the item
        update_response = self.client.put(
            f'/items/{item_id}/',
            {
                "title": "Updated Task",
                "description": "Updated description",
                "due_date": "2024-12-20",
                "status": "COMPLETED",
                "tags": ["home", "updated"]
            },
            format='json'
        )
        self.assertEqual(update_response.status_code, 202)

        # delete the item
        delete_response = self.client.delete(f'/items/{item_id}/')
        self.assertEqual(delete_response.status_code, 204)

        # check if the item is deleted
        get_item_response = self.client.get(f'/items/{item_id}/')
        self.assertEqual(get_item_response.status_code, 404)
