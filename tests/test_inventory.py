from django.test import TestCase
from rest_framework.test import APIClient
from apps.pets.models import Category, Pet
from apps.stores.models import Store


client = APIClient()

# Create your tests here.
store_data = {
    "id": 1,
    "petId": 1,
    "quantity": 1,
    "shipDate": "2020-01-01T00:00:00.000Z",
    "status": "placed",
    "complete": True
}

class StoreTest(TestCase):
    def setUp(self):
        # create a pet category
        self.category = Category.objects.create(
            id=1,
            name='pet_category',
        )

        self.pet = Pet.objects.create(
            id=1,
            name='dog',
            category=self.category,
            photoUrls='https://www.google.com',
            status='available',
        )

        self.store = Store.objects.create(
            id=1,
            petId=self.pet,
            quantity=1,
            shipDate="2020-01-01T00:00:00.000Z",
            status="placed",
            complete=True
        )

    def test_get_store(self):
        res = client.get('/store/', format='json')
        # has status placed
        self.assertEqual(Store.objects.get(id=1).id, 1)
        self.assertEqual(res.status_code, 200)

    def test_get_store_by_id(self):
        res = client.get('/store/1/', format='json')
        self.assertEqual(res.status_code, 200)