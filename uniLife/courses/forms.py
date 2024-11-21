from django import forms
from .models import Course, Keyword

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'content', 'learned', 'images']

class KeywordForm(forms.ModelForm):
    class Meta:
        model = Keyword
        fields = ['course', 'english', 'turkish', 'norwegian', 'image']
