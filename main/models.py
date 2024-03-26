import self as self
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.text import slugify


# Create your models here.
def validate_no_digits(value):
    if any(char.isdigit() for char in value):
        raise ValidationError('Поле не должно содержать цифры.')

def clean_name(self):
    name = self.cleaned_data['name']
    if not name:
        raise forms.ValidationError('Поле не должно быть пустым.')
    return name

class News(models.Model):
    name = models.CharField('Name:', max_length=30, validators=[validate_no_digits, clean_name])
    category = models.CharField('Category:', max_length=50, validators=[validate_no_digits, clean_name])
    full_text = models.TextField('Publication:', max_length=200, validators=[clean_name])
    date = models.DateTimeField('Publication date:', validators=[clean_name])
    slug = models.SlugField(null=False, unique=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            # Генерация слага на основе заголовка статьи
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}_________________{self.category}_______________{self.full_text}____________________________{self.date}'


class SuperModel(models.Model):
    login = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class MyModel(models.Model):
    my_file = models.FileField(upload_to='files/')
    my_image = models.ImageField(upload_to='images/')


class VisitedPage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    page_name = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} visited {self.page_name} at {self.timestamp}"
