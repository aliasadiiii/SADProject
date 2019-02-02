from datetime import date, timedelta
from model_mommy import mommy

from django.test import TestCase
from django.contrib.auth.models import User

from account.models import Account
from .models import Product, ProductKind, Comment


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


class ProductPageTestCase(TestCase):
    def setUp(self):
        product_kind = mommy.make(ProductKind, name='test')
        self.product = mommy.make(Product, name='test',
                                  kind=product_kind, price=1000,
                                  expires_at=date.today() + timedelta(3))
        user = mommy.make(User, username='test')
        user.set_password('test')
        user.save()
        self.account = mommy.make(Account, user=user)

    def test_product_page(self):
        response = self.client.get('/product/{}/'.format(self.product.id))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['product']['name'], self.product.name)
        self.assertEqual(response.context['product']['price'],
                         self.product.price)
        self.assertEqual(response.context['product']['product_id'],
                         self.product.id)

        self.assertEqual(response.context['account'], None)

    def test_authenticated_product_page(self):
        self.client.login(username='test', password='test')
        response = self.client.get('/product/{}/'.format(self.product.id))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['account'], self.account)

    def test_comment(self):
        mommy.make(Comment, product=self.product, author=self.account,
                   approved=True)
        response = self.client.get('/product/{}/'.format(self.product.id))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context['comments'].values_list('id', flat=True)),
            list(Comment.objects.all().values_list('id', flat=True)))


class AddCommentTestCase(TestCase):
    def setUp(self):
        product_kind = mommy.make(ProductKind, name='test')
        self.product = mommy.make(Product, name='test',
                                  kind=product_kind, price=1000,
                                  expires_at=date.today() + timedelta(3))
        user = mommy.make(User, username='test')
        user.set_password('test')
        user.save()
        self.account = mommy.make(Account, user=user)

    def test_add_comment(self):
        self.client.login(username='test', password='test')
        response = self.client.post(
            '/product/{}/post_comment/'.format(self.product.id), {
                'text': 'test'
            })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Comment.objects.count(), 1)
        comment = Comment.objects.all()[0]
        self.assertEqual(comment.author, self.account)
        self.assertEqual(comment.product, self.product)
        self.assertEqual(comment.text, 'test')
