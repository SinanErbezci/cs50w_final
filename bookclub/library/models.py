from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateField()
    author = models.ManyToManyField('Author', related_name='books')
    pages = models.SmallIntegerField()
    category = models.ManyToManyField('Category', related_name="category")

    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=100)
    birth = models.DateField()

    def __str__(self):
        return self.name

class Category(models.Model):
        CATEGORY_CHOICES = {
        "FI": "Fiction",
        "HI": "Historical Fiction",
        "MY": "Mystery & Thriller",
        "RO": "Romance",
        "RM": "Romantasy",
        "FA": "Fantasy",
        "SC": "Science Fiction",
        "HO": "Horror",
        "YO": "Young Adult Fantasy",
        "YU": "Young Adult Fiction",
        "DE": "Debut Novel",
        "NO": "Nonfiction",
        "ME": "Memoir & Autobiography",
        "HI": "History & Biography",
        "HU": "Humor"    
        }
        name = models.CharField(max_length=2, choices=CATEGORY_CHOICES)