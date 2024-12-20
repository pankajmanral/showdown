from django.test import TestCase,Client
from django.urls import reverse
from django.contrib.auth.models import User

class CartTest(TestCase):
    def setUp(self):
        self.client = Client()
        User.objects.create_user(username='admin',password='123')
        self.client.post(reverse('login'),{'username':'admin','password':'123'})

    def test_get_cart(self):
        response = self.client.get(reverse('cart'))
        self.assertTemplateUsed(response,'cart/cart.html')