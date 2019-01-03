from model_mommy import mommy

from django.contrib.auth.models import User
from django.test import TestCase

from .models import Account


class ActivateTestCase(TestCase):
    def test_activate_successful(self):
        user = mommy.make(User, username='test', email='test', is_active=False)
        mommy.make(Account, user=user, phone='09120000000', token='test')

        response = self.client.get('/account/activate/?token=test')
        self.assertEqual(response.status_code, 302)
        user.refresh_from_db()
        self.assertTrue(user.is_active)


    def test_activate_fail(self):
        response = self.client.get('/account/activate/?token=test')
        self.assertEqual(response.status_code, 404)
