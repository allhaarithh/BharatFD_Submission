# faq_management/admin.py
from django.contrib import admin
from .models import FAQ

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'get_languages')
    
    def get_languages(self, obj):
        return f"EN, HI, BN"
    get_languages.short_description = 'Languages'