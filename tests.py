from django.test import TestCase, Client
from django.urls import reverse

class GeneralSiteTests(TestCase):
    """Test cases for general site functionality"""
    
    def setUp(self):
        self.client = Client()
    
    def test_404_page(self):
        """Test that 404 page is displayed for non-existent URLs"""
        response = self.client.get('/this-page-does-not-exist/')
        self.assertEqual(response.status_code, 404)
    
    def test_homepage_exists(self):
        """Test that homepage loads successfully"""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
    
    def test_navigation_links(self):
        """Test that main navigation links are working"""
        urls = [
            reverse('index'),
            reverse('classes'),
            reverse('contact'),
            reverse('my_account'),
        ]
        
        for url in urls:
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)
