from django.urls import path
from . import views

urlpatterns = [
    # Ders yolları
    path('', views.index, name='index'),  # Kurs listesi (index sayfası)
    path('course/new/', views.course_create, name='course_create'),  # Yeni kurs ekleme
    path('course/<int:pk>/', views.course_detail, name='course_detail'),  # Kurs detayı
    path('course/<int:pk>/edit/', views.course_edit, name='course_edit'),  # Kurs düzenleme
    path('course/<int:pk>/delete/', views.course_delete, name='course_delete'),  # Kurs silme

    # Anahtar Kelime yolları
    path('keyword/new/', views.keyword_create, name='keyword_create'),  # Yeni kelime ekleme
    path('keywords/', views.keyword_list, name='keyword_list'),  # Anahtar kelime listesi
    path('keyword/<int:pk>/edit/', views.keyword_edit, name='keyword_edit'),  # Kelime düzenleme
    path('keyword/<int:pk>/delete/', views.keyword_delete, name='keyword_delete'),  # Kelime silme
]
