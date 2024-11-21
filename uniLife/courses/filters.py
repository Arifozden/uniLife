# filters.py
import django_filters
from .models import Keyword
from django.db.models import Q

class KeywordFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='filter_by_word')

    class Meta:
        model = Keyword
        fields = ['course']  # sadece course üzerinden filtreleme yapılabilir

    def filter_by_word(self, queryset, name, value):
        if value:
            # 'value' kullanıcının arama kelimesi
            return queryset.filter(
                Q(english__icontains=value) | 
                Q(turkish__icontains=value) | 
                Q(norwegian__icontains=value)
            )
        return queryset
