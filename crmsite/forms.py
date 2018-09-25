from django import forms
from django.core.validators import RegexValidator
from django.forms import CheckboxInput

from .models import *

textValidator = RegexValidator(r"[а-яА-Яa-zA-Z]",
                               "Поле должно содержать символы")
tagsValidator = RegexValidator(r"[а-яА-Яa-zA-Z]",
                               "Tags should contain letters")
passwordValidator = RegexValidator(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$",
                                   "Пароль должен содержать минимум 8 символов, 1 букву и 1 цифру как минимум ")


class UserSignUpForm(forms.Form):
    first_name = forms.CharField(validators=[textValidator],
                                 label="Имя",
                                 widget=forms.TextInput(attrs={'class': 'form-control',
                                                               'minlength': 2,
                                                               'maxlength': 30,
                                                               'placeholder': 'Имя'}))
    last_name = forms.CharField(validators=[textValidator],
                                label="Фамилия",
                                widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'minlength': 2,
                                                              'maxlength': 30,
                                                              'placeholder': 'Фамилия'}))
    username = forms.CharField(validators=[textValidator],
                               label="Никнейм",
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'minlength': 5,
                                                             'maxlength': 30,
                                                             'placeholder': 'Никнейм'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control',
                                                            'placeholder': 'E-mail'}))
    password = forms.CharField(validators=[passwordValidator],
                               label="Пароль",
                               widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'Пароль'}))
    password_confirmation = forms.CharField(label="Потверждение пароля",
                                            widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                              'placeholder': 'Подтверждение пароля'}))
    position = forms.ChoiceField(choices=(
        ('Студент', 'Студент'), ('Преподаватель', 'Преподаватель'), ('Научный сотрудник', 'Научный сотрудник')),
        label="Должность ")
    caf = forms.CharField(label="Кафедра ")
    bio = forms.CharField(label="Биография ")
    phoneNumber = forms.CharField(label="Номер телефона ")
    commentForAdmin = forms.CharField(label="Комментарии администратору ")


class NewOrderForm(forms.Form):
    nameJob = forms.CharField(label="Название работы")
    annotation = forms.CharField(label="Аннотация")
    keyWords = forms.CharField(label="Ключевые слова")
    TRUE_FALSE_CHOICES = (
        (True, 'Yes'),
        (False, 'No')
    )
    isAnalyst = forms.BooleanField(label="Требуется аналитик")
    isConsult = forms.BooleanField(label="Требуется консультант")
    isTranslator = forms.BooleanField(label="Требуется переводчик")
    isEditor = forms.BooleanField(label="Требуется редактор")
    Comment = forms.CharField(label="Комментарий")
    BlackFile = forms.FileField(label="черновой вариант документа",required=False)


class AdminPanelForm(forms.Form):
    garantAc = forms.BooleanField(label="Подтверждение аккаунта")
    isAuthor = forms.BooleanField(label="Автор")
    isModerator = forms.BooleanField(label="Модератор")
    isHead = forms.BooleanField(label="Руководитель")
    isAdmin = forms.BooleanField(label="Администратор")
    isChefEditor = forms.BooleanField(label="Директор")
    isAnalyst = forms.BooleanField(label="Аналитик")
    isConsult = forms.BooleanField(label="Консультант")
    isTranslator = forms.BooleanField(label="Переводчик")
    isChefTranslator = forms.BooleanField(label="Шеф переводчик")
    isEditor = forms.BooleanField(label="Требуется редактор")

class ModeratorPanelForm(forms.Form):
    nameJob = forms.CharField(label="Название работы", required=False)
    annotation = forms.CharField(label="Аннотация", required=False)
    keyWords = forms.CharField(label="Ключевые слова", required=False)
    TRUE_FALSE_CHOICES = (
        (True, 'Yes'),
        (False, 'No')
    )
    isAnalyst = forms.BooleanField(label="Требуется аналитик", required=False)
    isConsult = forms.BooleanField(label="Требуется консультант", required=False)
    isTranslator = forms.BooleanField(label="Требуется переводчик", required=False)
    isEditor = forms.BooleanField(label="Требуется редактор", required=False)
    Comment = forms.CharField(label="Комментарий", required=False)
    BlackFile = forms.FileField(label="черновой вариант документа", required=False)
    LastFile = forms.FileField(label="Последний вариант документа", required=False)