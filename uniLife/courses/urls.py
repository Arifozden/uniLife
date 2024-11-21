from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('course/new/', views.course_create, name='course_create'),
    path('course/<int:pk>/', views.course_detail, name='course_detail'),
    path('keyword/new/', views.keyword_create, name='keyword_create'),
    path('keywords/', views.keyword_list, name='keyword_list'),
]
