from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='вход'),
    path('logout/', views.logout, name='выход'),
    path('register/', views.register, name='регистрация'),
    path('profile/', views.profile, name='профиль'),
]