from datetime import date, timedelta
from model_mommy import mommy

from django.contrib.auth.models import User
from django.test import TestCase

from account.models import Account
from product.models import Product
from .models import Purchase, PurchaseItem


class AddItemTestCase(TestCase):
    def setUp(self):
        self.product = mommy.make(Product, name='test', price=1000,
                                  expires_at=date.today() + timedelta(3),
                                  is_available=True)
        user = mommy.make(User, username='test')
        user.set_password('test')
        user.save()
        self.account = mommy.make(Account, user=user)

    def test_add_item(self):
        self.client.login(username='test', password='test')
        response = self.client.post('/purchase/add/{}/'.format(self.product.id),
                                    {'amount': 10})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Purchase.objects.count(), 1)
        self.assertEqual(PurchaseItem.objects.count(), 1)


class EditItemTestCase(TestCase):
    def setUp(self):
        self.product = mommy.make(Product, name='test', price=1000,
                                  expires_at=date.today() + timedelta(3),
                                  is_available=True)
        user = mommy.make(User, username='test')
        user.set_password('test')
        user.save()
        self.account = mommy.make(Account, user=user)

        mommy.make(PurchaseItem, product=self.product, purchase__user=user)

    def test_edit_item(self):
        self.client.login(username='test', password='test')
        response = self.client.post(
            '/purchase/edit/{}/'.format(self.product.id), {'amount': 10})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(PurchaseItem.objects.count(), 1)

        purchase_item = PurchaseItem.objects.all()[0]
        self.assertEqual(purchase_item.purchase.user, self.account.user)
        self.assertEqual(purchase_item.amount, 10)


class DeleteItemTestCase(TestCase):
    def setUp(self):
        self.product = mommy.make(Product, name='test', price=1000,
                                  expires_at=date.today() + timedelta(3),
                                  is_available=True)
        user = mommy.make(User, username='test')
        user.set_password('test')
        user.save()
        self.account = mommy.make(Account, user=user)

        mommy.make(PurchaseItem, product=self.product, purchase__user=user)

    def test_delete_item(self):
        self.client.login(username='test', password='test')
        response = self.client.get(
            '/purchase/delete/{}/'.format(self.product.id))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(PurchaseItem.objects.count(), 0)
