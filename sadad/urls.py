from django.urls import path, include
from news import views

urlpatterns = [
    path('', views.news_list, name='home'),  # Add a default URL pattern for the empty path
    path('news_list/', views.news_list, name='news_list'),
    path('news_search/', views.news_search, name='news_search'),
    path('news_create/', views.news_create, name='news_create'),
    path('news_edit/<int:pk>/', views.news_edit, name='news_edit'),
    path('news_delete/<int:pk>/', views.news_delete, name='news_delete'),
]
