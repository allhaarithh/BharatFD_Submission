# faq_management/serializers.py
from rest_framework import serializers
from .models import FAQ

class FAQSerializer(serializers.ModelSerializer):
    translated_question = serializers.SerializerMethodField()
    translated_answer = serializers.SerializerMethodField()

    class Meta:
        model = FAQ
        fields = ['id', 'translated_question', 'translated_answer']

    def get_translated_question(self, obj):
        lang = self.context.get('request').query_params.get('lang', 'en')
        return obj.get_translated_question(lang)

    def get_translated_answer(self, obj):
        lang = self.context.get('request').query_params.get('lang', 'en')
        return obj.get_translated_answer(lang)