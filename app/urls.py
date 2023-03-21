from django.urls import path
from app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('SignIn', views.sign, name='sign'),
    path('about', views.About, name='About'),
    
]
