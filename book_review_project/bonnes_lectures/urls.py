from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('', views.welcome, name='welcome'),
      path('book/', views.book_list, name='book_list'), 
]