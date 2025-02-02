# faq_management/views.py
from rest_framework import viewsets
from django.core.cache import cache
from .models import FAQ
from .serializers import FAQSerializer

class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def get_queryset(self):
        lang = self.request.query_params.get('lang', 'en')
        cache_key = f'faqs_{lang}'
        
        # Check cache first
        cached_faqs = cache.get(cache_key)
        if cached_faqs is not None:
            return cached_faqs
        
        # If not in cache, fetch and cache
        queryset = super().get_queryset()
        cache.set(cache_key, queryset, timeout=3600)  # Cache for 1 hour
        return queryset