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
    path('moderating/', views.moderator_panel, name='Панель управления заявками'),
    path('moderating/<int:ids>', views.moderatorOrderEdit, name='Управление заявкой'),
    path('download/<int:ids>', views.download, name='загрузка'),

    path('moderatingS/', views.moderator_panel, name='Панель управления заявками'),
    path('moderatingS/<int:ids>', views.moderatorOrderEdit, name='Управление заявкой'),

    path('translator/', views.show, name="Заявки на перевод"),
    path('translator/<int:ids>', views.showEdit, name="Заявка на перевод"),
    path('analyst/', views.show, name="Заявки на Анализ"),
    path('analyst/<int:ids>', views.showEdit, name="Заявки на Анализ"),
    path('consultant/', views.show, name="Заявки на Консультацию"),
    path('consultant/<int:ids>', views.showEdit, name="Заявки на Консультацию"),
    path('editor/', views.show, name="Заявки на Консультацию"),
    path('editor/<int:ids>', views.showEdit, name="Заявки на Консультацию"),

    path('translatorS/', views.show, name="Заявки на перевод"),
    path('translatorS/<int:ids>', views.showEdit, name="Заявка на перевод"),
    path('analystS/', views.show, name="Заявки на Анализ"),
    path('analystS/<int:ids>', views.showEdit, name="Заявки на Анализ"),
    path('consultantS/', views.show, name="Заявки на Консультацию"),
    path('consultantS/<int:ids>', views.showEdit, name="Заявки на Консультацию"),
    path('editorS/', views.show, name="Заявки на Консультацию"),
    path('editorS/<int:ids>', views.showEdit, name="Заявки на Консультацию"),

]