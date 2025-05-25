from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class SignupViewTest(TestCase):
    def test_user_can_sign_up(self):
        test_username = 'Test_User'
        test_pass = 'Test123!'
        
        # Create user using signup endpoint
        response = self.client.post(reverse('signup'), {
            'username': test_username,
            'password1': test_pass,
            'password2': test_pass,
        })

        # Check redirect to home
        self.assertRedirects(response, reverse('home'))

        # User should exist now
        user_exists = User.objects.filter(username=test_username).exists()
        self.assertTrue(user_exists)
