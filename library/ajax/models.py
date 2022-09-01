from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    father_name = models.TextField(blank=True, max_length=150)
# Create your models here.


class Book(models.Model):
    title = models.CharField(
        max_length=256,
        db_index=True,
        verbose_name='Название'
    )
    year = models.IntegerField(
        verbose_name='Год написания'
    )
    description = models.TextField(verbose_name='Описание книги', max_length=1024)

    def __str__(self):
        return self.title