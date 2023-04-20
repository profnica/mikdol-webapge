from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('success/', views.success, name="success"),
    path('Subsuccess/', views.Subsuccess, name="Subsuccess"),
    path('subscribe/', views.subscribe, name="subscribe"),
]
