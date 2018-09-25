from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='вход'),
    path('logout/', views.logout, name='выход'),
    path('register/', views.register, name='регистрация'),
    path('profile/', views.profile, name='профиль'),
    path('neworder/', views.createOrder, name='новая заявка'),
    path('orders/', views.orders, name='заявки'),
    path('orders/<int:ids>', views.orders_detail, name='детали заявки'),
    path('admining/', views.adminPanel, name='Панель управления пользователями'),
    path('admining/<int:ids>', views.user_detail_admin, name='Панель управления пользователем'),

]