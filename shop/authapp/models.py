from django.db import models
from django.contrib.auth.models import User, AbstractUser

class Custom_User(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', verbose_name='аватарка', blank=True)
    age = models.PositiveIntegerField(verbose_name='возраст')
    