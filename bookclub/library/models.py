from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
# Create your models here.

class User(AbstractUser):
    pass

class Book(models.Model):

    #bookID, title, authors, average_rating, language_code, ratings_count, text_reviews_count, publication_date, publisher
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=10000)
    pub_date = models.DateField()
    author = models.ManyToManyField('Author', related_name='books')
    pages = models.SmallIntegerField()


    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Genres(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Series(models.Model):
    name = models.CharField(max_length=100)
    number = models.SmallIntegerField()

    def __str__(self):
        return self.name
    
class Publisher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name