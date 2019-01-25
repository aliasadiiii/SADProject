from datetime import date, timedelta
from model_mommy import mommy

from django.test import TestCase

from .models import Product, ProductKind


class ProductListTestCase(TestCase):
    def setUp(self):
        product_kind = mommy.make(ProductKind, name='test')
        mommy.make(Product, name='test', kind=product_kind,
                   price=1000, expires_at=date.today() + timedelta(3))

    def test_product_list(self):
        response = self.client.get('/product/list/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['products']), 1)
        self.assertEqual(response.context['kinds'], ['test'])

    def test_product_list_with_filter(self):
        response = self.client.get('/product/list/?kind=an')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['products'], [])
        self.assertEqual(response.context['kinds'], ['test'])

        response = self.client.get('/product/list/?kind=test')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['products']), 1)
