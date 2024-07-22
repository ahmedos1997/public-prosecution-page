from django.contrib import admin
from django.urls import path , include
from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('news', views.news, name='news'),
    path('news_view/<int:id>', views.news_view, name='news_view'),
    path('attorney_general', views.attorney_general, name='attorney_general'),
    path('attorney_general/<int:id>', views.attorney_general_view, name='attorney_general_view'),
    path('change-language/', views.change_language, name='change_language'),
]