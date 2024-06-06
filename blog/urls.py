from django.urls import path
from blog import views

# blog routes URLs
urlpatterns = [
    path('example/', views.example, name='example'),
    path('articles/', views.articles, name='articles'),
    path('article/<int:id>', views.article, name='article')
]