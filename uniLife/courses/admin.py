# admin.py

from django.contrib import admin
from .models import Course, Keyword, Category, Tag

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'content']
    filter_horizontal = ['categories', 'tags']  # Çoklu seçim için filtreleme

class KeywordAdmin(admin.ModelAdmin):
    list_display = ['word', 'course']
    filter_horizontal = ['tags']  # Etiketler için filtreleme

admin.site.register(Course, CourseAdmin)
admin.site.register(Keyword, KeywordAdmin)
admin.site.register(Category)
admin.site.register(Tag)
