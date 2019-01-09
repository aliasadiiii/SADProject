from model_mommy import mommy

from django.contrib.auth.models import User
from django.core import mail
from django.test import TestCase

from .models import Account


class ActivateTestCase(TestCase):
    def test_activate_successful(self):
        user = mommy.make(User, username='test', email='test@test.com',
                          is_active=False)
        mommy.make(Account, user=user, phone='09120000000',
                   activation_token='test')

        response = self.client.get('/account/activate/?token=test')
        self.assertEqual(response.status_code, 302)
        user.refresh_from_db()
        self.assertTrue(user.is_active)

    def test_activate_fail(self):
        response = self.client.get('/account/activate/?token=test')
        self.assertEqual(response.status_code, 404)


class ForgetPasswordTestCase(TestCase):
    def setUp(self):
        user = mommy.make(User, username='test', email='test@test.com',
                          is_active=False)
        self.account = mommy.make(Account, user=user, phone='09120000000')

    def test_forget_password(self):
        self.client.post('/account/forget_password/', data={
            'email': 'test@test.com'
        })
        self.assertEqual(len(mail.outbox), 1)

        self.account.refresh_from_db()
        self.client.post(
            '/account/change_password/?token={}'.format(
                self.account.forget_password_token),
            data={'password1': 'testtest', 'password2': 'testtest'}
        )

        self.account.user.refresh_from_db()
        self.assertTrue(self.account.user.check_password('testtest'))
