from django.urls import path
from blog import views

# blog routes URLs
urlpatterns = [
    path('articles/', views.articles, name='articles')
]