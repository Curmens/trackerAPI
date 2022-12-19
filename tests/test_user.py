from django.test import TestCase
from rest_framework.test import APIClient
from apps.user.models import User

client = APIClient()

# Create your tests here.
users = [
    {
        "id": 10,
        "username": "theUser1024",
        "firstName": "John",
        "lastName": "James",
        "email": "johasn@emailsasdf.com",
        "password": "12345",
        "phone": "12345",
        "userStatus": 0
    },
    {
        "id": 11,
        "username": "theUser2",
        "firstName": "John2",
        "lastName": "James2",
        "email": "admin@email.com",
        "password": "12345",
        "phone": "12345",
        "userStatus": 0
    },
    {
        "id": 12,
        "username": "theUser3",
        "firstName": "John3",
        "lastName": "James3",
        "email": "hello@gmail.com",
        "password": "12345",
        "phone": "12345",
        "userStatus": 0
    }
]

class UserTest(TestCase):
    def setUp(self):
        # create a user
        self.user = User.objects.create_user(
            username='theUser10244',
            firstName='John',
            lastName='James',
            email='admin@test.com',
            password='12345',
            phone='12345',
            userStatus=0
        )

    def test_create_user(self):
        res = client.post('/user/createWithList/', data=users, format='json')
        self.assertEqual(res.status_code, 201)

    def test_login_user(self):
        res = client.post('/user/login/', data={'username': 'theUser10244', 'password': '12345'}, format='json')
        self.assertEqual(res.status_code, 200)

    def test_get_user(self):
        res = client.get('/user/username/theUser10244/')
        self.assertEqual(res.status_code, 200)

    def test_update_user(self):
        res = client.put('/user/username/theUser10244/', data=users[0], format='json')
        self.assertEqual(res.status_code, 201)

    def test_delete_user(self):
        res = self.client.delete('/user/username/theUser10244/')
        self.assertEqual(res.status_code, 200)