# tests/test_faq.py
import pytest
from django.test import TestCase
from faq_management.models import FAQ

@pytest.mark.django_db
class TestFAQModel(TestCase):
    def test_translation(self):
        faq = FAQ.objects.create(
            question="What is Django?", 
            answer="Django is a web framework"
        )
        
        # Test default language
        assert faq.get_translated_question() == "What is Django?"
        
        # Test translations
        assert faq.get_translated_question('hi') is not None
        assert faq.get_translated_question('bn') is not None