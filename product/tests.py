from django.test import TestCase

from .models import *
from django.db import models


class ArticleModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        Article.objects.create(code='test_name', description='test_description', replacement_price='350')

    def test_article_replacement_price_is_an_integer(self):
        article = Article.objects.get(id=1)
        replacement_price = article._meta.get_field('replacement_price')
        print(replacement_price)
        self.assertTrue(isinstance(replacement_price, models.IntegerField))

    def test_article_code_max_length_equals_20(self):
        article = Article.objects.get(id=1)
        code = article._meta.get_field('code')
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
        art = Article.objects.create(code='test_name', description='test_description', replacement_price='350')
        cat = Category.objects.create(name='test_name', icon='icon.png')
        Product.objects.create(article=art, category=cat, price=350)

    def test_order_date_delivery_is_5_days_past_to_date_order(self):
        product = Product.objects.get(id=1)
        user = User.objects.get(username='test@test.com')
        order = Order.objects.create(client=user, product=product)
        self.assertEqual(order.date_delivery - order.date_order, timezone.timedelta(days=5))
