from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone




class Worker(models.Model):
    isAuthor = models.BooleanField(default=True)
    isAdmin = models.BooleanField()
    isModerator = models.BooleanField()
    isAnalyst = models.BooleanField()
    isConsult = models.BooleanField()
    isChefEditor = models.BooleanField
    isEditor = models.BooleanField
    isChefTranslator = models.BooleanField
    isTranslator = models.BooleanField

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
    position = models.CharField(max_length=10, choices=types)
    garantAc = models.BooleanField(default=False)
    commentForAdmin = models.TextField


    def publish(self):
        self.adddate = timezone.now()
        self.save()

    def __str__(self):
        return self.username


class Orders(models.Model):
    nameJob = models.CharField(max_length=100)
    createAt = models.DateTimeField(default=timezone.now)
    updateAt = models.DateTimeField(default=timezone.now)
    annotation = models.TextField
    typeOfWork = models.TextField
    keyWords = models.TextField
    Comment = models.TextField
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True,related_name='+')
    moderator = models.ForeignKey(User, on_delete=models.CASCADE, null=True,related_name='+')
    isAnalyst = models.BooleanField()
    isConsult = models.BooleanField()
    isTranslator = models.BooleanField()
    isEditor = models.BooleanField()
    Analyst = models.ForeignKey(User, on_delete=models.CASCADE, null=True,related_name='+')
    Consult = models.ForeignKey(User, on_delete=models.CASCADE, null=True,related_name='+')
    Translator = models.ForeignKey(User, on_delete=models.CASCADE, null=True,related_name='+')
    Editor = models.ForeignKey(User, on_delete=models.CASCADE, null=True,related_name='+')
    BlackFile = models.FileField(upload_to="BlackFile")
    LastFile = models.FileField(upload_to="LastFile")