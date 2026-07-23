from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80.00, inventory=100)
        # Verify the __str__ outputs exactly as formatted to two decimals
        self.assertEqual(str(item), "IceCream : 80.00")
