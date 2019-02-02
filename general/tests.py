from django.test import TestCase


class GeneralTestCase(TestCase):
    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_us(self):
        response = self.client.get('/about-us/')
        self.assertEqual(response.status_code, 200)
