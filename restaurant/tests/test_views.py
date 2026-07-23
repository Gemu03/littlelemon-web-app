from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.item1 = Menu.objects.create(title="IceCream", price=80.00, inventory=100)
        self.item2 = Menu.objects.create(title="Salad", price=10.50, inventory=50)

    def test_getall(self):
        url = reverse('menu_items')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Verify serialized list is correct
        menus = Menu.objects.all().order_by('title')
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.data, serializer.data)
