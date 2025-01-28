from django.test import TestCase, Client
from django.urls import reverse
from .models import ContactMessage
from .forms import ContactForm

# Create your tests here.

class ContactModelTests(TestCase):
    """Test cases for the Contact Message model"""
    
    def test_create_message(self):
        """Test that we can create a contact message"""
        message = ContactMessage.objects.create(
            name="John Doe",
            email="john@example.com",
            message="Hello, this is a test message"
        )
        # Check if the message was saved correctly
        self.assertEqual(message.name, "John Doe")
        self.assertEqual(message.email, "john@example.com")
        self.assertEqual(message.message, "Hello, this is a test message")

class ContactViewTests(TestCase):
    """Test cases for the contact view"""
    
    def setUp(self):
        """Setup runs before each test method"""
        self.client = Client()
    
    def test_contact_page_loads(self):
        """Test that contact page loads correctly"""
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')
    
    def test_contact_form_submission(self):
        """Test submitting the contact form"""
        form_data = {
            'name': 'Jane Doe',
            'email': 'jane@example.com',
            'message': 'This is a test message'
        }
        response = self.client.post(reverse('contact'), form_data)
        # Check if message was saved to database
        self.assertEqual(ContactMessage.objects.count(), 1)
        # Check if the form submission was successful
        self.assertEqual(response.status_code, 302)  # 302 is redirect status code

    def test_invalid_email_format(self):
        """Test that invalid email addresses are rejected"""
        form_data = {
            'name': 'Test User',
            'email': 'invalid-email',  # Invalid email format
            'message': 'Test message'
        }
        response = self.client.post(reverse('contact'), form_data)
        self.assertFormError(response, 'form', 'email', 'Enter a valid email address.')

    def test_required_fields(self):
        """Test that all required fields must be filled"""
        form_data = {
            'name': '',  # Empty required field
            'email': 'test@example.com',
            'message': ''  # Empty required field
        }
        response = self.client.post(reverse('contact'), form_data)
        self.assertFormError(response, 'form', 'name', 'This field is required.')
        self.assertFormError(response, 'form', 'message', 'This field is required.')

class ContactTemplateTests(TestCase):
    """Test cases for the contact template"""
    
    def setUp(self):
        self.client = Client()
    
    def test_contact_form_exists(self):
        """Test that the contact form appears on the page"""
        response = self.client.get(reverse('contact'))
        self.assertContains(response, '<form')
        self.assertContains(response, 'name="name"')
        self.assertContains(response, 'name="email"')
        self.assertContains(response, 'name="message"')