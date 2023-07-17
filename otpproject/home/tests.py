from django.test import SimpleTestCase
from django.urls import reverse,resolve
from home.views import home,contact, subscription_email,about,cart,search,wishlist,terms


# Create your tests here.
class Testurls(SimpleTestCase):
    def test_case_home_urls(self):
        urls= reverse('home')
        self.assertEquals(resolve(urls).func,home)


     
    def test_case_contact_urls(self):
        urls= reverse('contact')
        self.assertEquals(resolve(urls).func,contact) 

    
    def test_case_subscription_email_urls(self):
        urls= reverse('subscription_email')
        self.assertEquals(resolve(urls).func,subscription_email)


    def test_case_about_urls(self):
        urls= reverse('about')
        self.assertEquals(resolve(urls).func,about)

    
    def test_case_cart_urls(self):
        urls= reverse('cart')
        self.assertEquals(resolve(urls).func,cart)

    def test_case_search_urls(self):
        urls= reverse('search')
        self.assertEquals(resolve(urls).func,search)

    def test_case_wishlist_urls(self):
        urls= reverse('wishlist')
        self.assertEquals(resolve(urls).func,wishlist)

    def test_case_terms_urls(self):
        urls= reverse('terms')
        self.assertEquals(resolve(urls).func,terms)
    
