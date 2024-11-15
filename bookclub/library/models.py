from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
# Create your models here.

class User(AbstractUser):
    MALE = "M"
    FEMALE = "F"
    OTHER = "O"

    GENDER_CHOICES = {
        MALE : "Male",
        FEMALE : "Female",
        OTHER : "Other"
    }

    birth_date = models.DateField(null=True, blank=True, default=None)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True, default=None)
    

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

    def __str__(self):
        return self.name
    
class Publisher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=10000,blank=True)
    pub_date = models.DateField(null=True, blank=True)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    pages = models.SmallIntegerField(blank=True, null=True)
    series = models.ForeignKey(Series,blank=True,null=True, on_delete=models.CASCADE, related_name='books')
    series_num = models.SmallIntegerField(blank=True, null=True)
    genres = models.ManyToManyField(Genres, blank=True, null=True, related_name='books')
    publisher = models.ForeignKey(Publisher, blank=True, null=True, on_delete=models.CASCADE, related_name='books')
    cover = models.URLField(blank=True, null=True)
    num_ratings = models.SmallIntegerField(default=0, blank=True)
    rating = models.DecimalField(default=0, max_digits=2, decimal_places=1)

    def __str__(self):
        return self.title