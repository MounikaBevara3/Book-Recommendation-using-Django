# recommend/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('recommend/', views.recommend_ui, name='recommend_ui'),
    path('recommend_books/', views.recommend_books, name='recommend_books'),
    path('list/', views.listt, name='listt'),
]
