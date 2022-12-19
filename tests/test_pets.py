from django.test import TestCase
from rest_framework.test import APIClient
from apps.pets.models import Category, Pet, Tags

client = APIClient()

# Create your tests here.
pet_data = {
        "name": "theUser1024",
        "category": 1,
        "photoUrls": "https://www.google.com",
        "status": "available"
}

class PetTest(TestCase):
    def setUp(self):
        # create a pet category
        self.category = Category.objects.create(
            id=1,
            name='pet_category',
        )

        # create a pet tag
        self.tag = Tags.objects.create(
            name='pet_tag',
        )

        self.pet = Pet.objects.create(
            name='dog',
            category=self.category,
            photoUrls='https://www.google.com',
            status='available',
        )

    def test_get_pet(self):
        res = client.get('/pet/find/', format='json')
        self.assertEqual(res.status_code, 200)