# faq_management/models.py
from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    
    # Language-specific translations
    question_hi = models.TextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)
    answer_hi = RichTextField(blank=True, null=True)
    answer_bn = RichTextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        translator = Translator()
        
        # Translate if translations are empty
        if not self.question_hi:
            self.question_hi = translator.translate(self.question, dest='hi').text
        if not self.question_bn:
            self.question_bn = translator.translate(self.question, dest='bn').text
        
        # Similar for answers
        if not self.answer_hi:
            self.answer_hi = translator.translate(self.answer, dest='hi').text
        if not self.answer_bn:
            self.answer_bn = translator.translate(self.answer, dest='bn').text
        
        super().save(*args, **kwargs)

    def get_translated_question(self, lang='en'):
        translations = {
            'en': self.question,
            'hi': self.question_hi or self.question,
            'bn': self.question_bn or self.question
        }
        return translations.get(lang, self.question)

    def get_translated_answer(self, lang='en'):
        translations = {
            'en': self.answer,
            'hi': self.answer_hi or self.answer,
            'bn': self.answer_bn or self.answer
        }
        return translations.get(lang, self.answer)