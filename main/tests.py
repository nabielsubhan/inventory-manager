from django.test import TestCase, Client
from main.models import Item

# Create your tests here.
class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

    def test_create_template(self):
        item = Item.objects.create(
            name="an item",
            amount="10",
            description="the total of this item is 10"
        )

        self.assertEqual(item.name, "an item")
        self.assertEqual(item.amount, "10")
        self.assertEqual(item.description, "the total of this item is 10")