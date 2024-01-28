from unittest import TestCase
from restaurant.models import Menu


class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=5, inventory=20)
        self.assertEqual(item, "IceCream : 80")
