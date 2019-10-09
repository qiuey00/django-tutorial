from django.test import TestCase
from .models import Person
# Create your tests here.

class PersonModelTest(TestCase):
	def test_added_content(self):
		aPerson = Person.objects.create(first_name="hi", last_name="hello", email="hi@hello.com")
		self.assertEqual(aPerson.first_name, "hi")
		self.assertEqual(aPerson.last_name, "hello")
		self.assertEqual(aPerson.email, "hi@hello.com")
