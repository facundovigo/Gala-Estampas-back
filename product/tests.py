from django.test import TestCase

from .models import *
from django.db import models


class SupplyModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        Supply.objects.create(code='test_name', description='test_description', replacement_price='350')

    def test_supply_replacement_price_is_an_integer(self):
        supply = Supply.objects.get(id=1)
        replacement_price = supply._meta.get_field('replacement_price')
        print(replacement_price)
        self.assertTrue(isinstance(replacement_price, models.IntegerField))

    def test_supply_code_max_length_equals_20(self):
        supply = Supply.objects.get(id=1)
        code = supply._meta.get_field('code')
        self.assertTrue(code, 20)


class ClientModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='test@test.com', password='password')
        Client.objects.create(user=user, birthdate='1966-06-06', address='calle falsa 123', state='Bs-As',
                              country='Argentina', zip_code='ab1234cd', telephone='01112345678')

    def test_client_have_foreingkey(self):
        client = Client.objects.get(id=1)
        user = User.objects.get(id=1)
        self.assertEqual(client.user, user)


class OrderModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create(username='test@test.com', password='password')
        art = Supply.objects.create(code='test_name', description='test_description', replacement_price='350')
        cat = Category.objects.create(name='test_name', icon='icon.png')
        Product.objects.create(supply=art, category=cat, price=350)

    def test_order_date_delivery_is_5_days_past_to_date_order_on_default_delivery_date(self):
        product = Product.objects.get(id=1)
        user = User.objects.get(username='test@test.com')
        order = Order.objects.create(client=user, product=product)
        self.assertEqual(order.date_delivery - order.date_order, timezone.timedelta(days=5))

    def test_order_date_delivery_cant_be_5_days_less_than_today(self):
        product = Product.objects.get(id=1)
        user = User.objects.get(username='test@test.com')
        invalid_date = datetime.date.today() + timezone.timedelta(days=3)
        invalid_order = Order.objects.create(client=user, product=product, date_delivery=invalid_date)
        self.assertRaisesMessage(invalid_order, 'date delivery must be 5 days greater than today')

    def test_order_date_delivery_can_be_5_days_greater_than_today(self):
        product = Product.objects.get(id=1)
        user = User.objects.get(username='test@test.com')
        valid_date = datetime.date.today() + timezone.timedelta(days=7)
        valid_order = Order.objects.create(client=user, product=product, date_delivery=valid_date)
        self.assertEqual(valid_order.date_delivery, valid_date)
