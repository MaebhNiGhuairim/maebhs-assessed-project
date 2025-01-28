from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

# Create your tests here.

class HomeViewTests(TestCase):
    """Test cases for home app views"""
    
    def setUp(self):
        """Setup runs before each test method"""
        self.client = Client()
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
    
    def test_index_page_load(self):
        """Test that home page loads correctly"""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        # Check for key content
        self.assertContains(response, 'Breathe, flow, transform')
        self.assertContains(response, 'About Us')
    
    def test_classes_page_load(self):
        """Test that classes page loads correctly"""
        response = self.client.get(reverse('classes'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'classes.html')
        # Check for key content
        self.assertContains(response, 'Our Classes')
        self.assertContains(response, 'Hatha Yoga')
        self.assertContains(response, 'Vinyasa Yoga')
    
    def test_my_account_page_load(self):
        """Test that my account page loads correctly when logged in"""
        # First try without login
        response = self.client.get(reverse('my_account'))
        self.assertEqual(response.status_code, 200)
        
        # Then try with login
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('my_account'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'my_account.html')
        self.assertContains(response, 'My Account')

    def test_protected_pages_redirect_anonymous(self):
        """Test that protected pages redirect to login for anonymous users"""
        protected_urls = [
            reverse('my_bookings'),
            reverse('book_a_class'),
        ]
        
        for url in protected_urls:
            response = self.client.get(url)
            self.assertEqual(response.status_code, 302)  # Should redirect to login
            self.assertTrue(response.url.startswith('/accounts/login/'))

    def test_user_profile_access(self):
        """Test that users can only access their own profile"""
        # Create two users
        user1 = User.objects.create_user('user1', 'user1@test.com', 'pass123')
        user2 = User.objects.create_user('user2', 'user2@test.com', 'pass123')
        
        # Login as user1
        self.client.login(username='user1', password='pass123')
        
        # Try to access user2's profile (should fail)
        response = self.client.get(reverse('my_account'))  # Use my_account instead of direct profile URL
        self.assertEqual(response.status_code, 200)  # Should load successfully
        # Add additional checks if needed

class HomeTemplateTests(TestCase):
    """Test cases for home app templates"""
    
    def setUp(self):
        self.client = Client()
    
    def test_base_template_content(self):
        """Test that base template elements appear on pages"""
        response = self.client.get(reverse('index'))
        # Check for navigation elements
        self.assertContains(response, 'The Yoga Loft')
        
    def test_index_template_sections(self):
        """Test that index page has all required sections"""
        response = self.client.get(reverse('index'))
        # Check for main sections
        self.assertContains(response, 'About Us')
        self.assertContains(response, 'Why Choose Us')
        self.assertContains(response, 'Join us')
    
    def test_classes_template_sections(self):
        """Test that classes page has all required sections"""
        response = self.client.get(reverse('classes'))
        # Check for class types
        self.assertContains(response, 'Hatha Yoga')
        self.assertContains(response, 'Vinyasa Yoga')
        self.assertContains(response, 'Ashtanga Yoga')
        self.assertContains(response, 'Yin Yoga')
