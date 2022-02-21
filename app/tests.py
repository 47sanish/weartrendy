from django.test import SimpleTestCase
from django.urls import reverse, resolve
from django.contrib.auth import views as auth_views

from app import views 

class TestUrls(SimpleTestCase):
# class 
    def test_base_url(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func.view_class, views.ProductView)
# function

    def test_add_to_cart_url(self):
        url = reverse('add-to-cart')
        self.assertEquals(resolve(url).func, views.add_to_cart)
        
    def test_my_buy_now_url(self):
        url = reverse('buy-now')
        self.assertEquals(resolve(url).func, views.buy_now)
        
    def test_my_profile_url(self):
        url = reverse('profile')
        self.assertEquals(resolve(url).func.view_class, views.ProfileView)

    def test_add_to_cart_url(self):
     url = reverse('address')
     self.assertEquals(resolve(url).func, views.address)

    def test_base_url(self):
     url = reverse('logout')
     self.assertEquals(resolve(url).func.view_class, auth_views.LogoutView)

    def test_base_url(self):
     url = reverse('passwordchange')
     self.assertEquals(resolve(url).func.view_class, auth_views.PasswordChangeView)

    def test_base_url(self):
     url = reverse('orders')
     self.assertEquals(resolve(url).func, views.orders)

    def test_base_url(self):
     url = reverse('mobile')
     self.assertEquals(resolve(url).func, views.mobile)

    def test_base_url(self):
     url = reverse('passwordchangedone')
     self.assertEquals(resolve(url).func.view_class, auth_views.PasswordChangeView)

    def test_base_url(self):
     url = reverse('password_reset')
     self.assertEquals(resolve(url).func.view_class, auth_views.PasswordResetView)

    def test_base_url(self):
     url = reverse('password_reset_done')
     self.assertEquals(resolve(url).func.view_class, auth_views.PasswordResetDoneView)        


