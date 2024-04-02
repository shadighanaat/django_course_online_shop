from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class SignupTest(TestCase):
    username = 'new_user_name'
    email = 'username@gmail.com'

    def test_signup_by_url(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='account/signup.html')

    def test_signup_url(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='account/signup.html')

    def test_signup_form(self):
        response = self.client.post(reverse('signup'), data={
            'username': self.username,
            'email': self.email,
        })

        users = get_user_model().objects.all()
        self.assertEqual(users.count(), 0)
        self.assertEqual(response.status_code, 200)
