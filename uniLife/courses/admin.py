from django.contrib import admin
from .models import Course, Keyword

# Modelleri admin paneline kaydet
admin.site.register(Course)
admin.site.register(Keyword)
