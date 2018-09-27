from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Worker(models.Model):
    isAuthor = models.BooleanField(default=False)
    isAdmin = models.BooleanField(default=False)
    isModerator = models.BooleanField(default=False)
    isAnalyst = models.BooleanField(default=False)
    isConsult = models.BooleanField(default=False)
    isChefEditor = models.BooleanField(default=False)
    isEditor = models.BooleanField(default=False)
    isChefTranslator = models.BooleanField(default=False)
    isTranslator = models.BooleanField(default=False)
    isHead = models.BooleanField(default=False)


class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    phoneNumber = models.CharField(max_length=11)
    role = models.ForeignKey(Worker, on_delete=models.CASCADE, null=True)
    caf = models.CharField(max_length=10)
    types = (
        ('Студент', 'Студент'),
        ('Преподаватель', 'Преподаватель'),
        ('Научный сотрудник', 'Научный сотрудник')
    )
    position = models.CharField(max_length=50, choices=types)
    garantAc = models.BooleanField(default=False)
    commentForAdmin = models.TextField(null=True)

    def publish(self):
        self.adddate = timezone.now()
        self.save()

    def __str__(self):
        return self.username


class Orders(models.Model):
    nameJob = models.CharField(max_length=100)
    createAt = models.DateTimeField(default=timezone.now)
    updateAt = models.DateTimeField(default=timezone.now, null=True)
    annotation = models.TextField(null=True)
    keyWords = models.TextField(null=True)
    Comment = models.TextField(null=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='+')
    moderator = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='+')
    isAnalyst = models.BooleanField(null=True)
    isConsult = models.BooleanField(null=True)
    isTranslator = models.BooleanField(null=True)
    isEditor = models.BooleanField(null=True)
    Analyst = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='+')
    Consult = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='+')
    Translator = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='+')
    Editor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='+')
    BlackFile = models.FileField(upload_to="BlackFile/", null=True)
    LastFile = models.FileField(upload_to="LastFile", null=True)
    aciveBy = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='+')
    types = (
        ('ПРИНЯТО В РАБОТУ', 'ПРИНЯТО В РАБОТУ'),
        ('ОТКЛОНЕНО', 'ОТКЛОНЕНО'),
        ('ПЕРЕДАНО КОНСУЛЬТАНТАМ', 'ПЕРЕДАНО КОНСУЛЬТАНТАМ'),
        ('ВОЗВРАЩЕНО АДМИНИСТРАТОРУ СИСТЕМЫ', 'ВОЗВРАЩЕНО АДМИНИСТРАТОРУ СИСТЕМЫ'),
        ('ПЕРЕДАНО РЕДАКТОРУ', 'ПЕРЕДАНО РЕДАКТОРУ'),
        ('ПЕРЕДАНО ПЕРЕВОДЧИКУ', 'ПЕРЕДАНО ПЕРЕВОДЧИКУ'),
        ('ПЕРЕДАННО АНАЛИТИКУ', 'ПЕРЕДАННО АНАЛИТИКУ'),
        ('ОТПРАВЛЕНО В ЖУРНАЛ', 'ОТПРАВЛЕНО В ЖУРНАЛ'),
        ('ПОЛУЧЕНО ИЗ ЖУРНАЛА НА ДОРАБОТКУ', 'ПОЛУЧЕНО ИЗ ЖУРНАЛА НА ДОРАБОТКУ'),
        ('В рассмотрении у администратора', 'В рассмотрении у администратора'),
        ('ПЕРЕДАНО МОДЕРАТОРУ', 'ПЕРЕДАНО МОДЕРАТОРУ'),
        ('Завершено', 'Завершено')
    )
    Condirion = models.TextField(null=True, choices=types)
    CHOISE = (
        ('1', 'У консультанта'),
        ('2', 'У редактора'),
        ('3', 'У переводчика'),
        ('4', 'У аналитика'),
    )
    StatusS = models.TextField(null=True, choices=CHOISE)
