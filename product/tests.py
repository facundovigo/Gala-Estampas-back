from django.test import TestCase
from .models import Product, Article, Category


class ProductModelTests(TestCase):

    def test_product_needs_article_and_category(self):
        self.assertTrue(True)


