from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Book(models.Model):
    class Category(models.TextChoices):
        FICTION = "FI", _("Fiction")
        HISTORICAL = "HI", _("Historical Fiction")
        MYSTERY = "MY", _("Mystery & Thriller")
        ROMANCE = "RO", _("Romance")
        ROMANTASY = "RM", ("Romantasy")
        FANTASY = "FA", _("Fantasy")
        SCIENCEFIC = "SC", _("Science Fiction")
        HORROR = "HO", _("Horror")
        YADULTFAN = "YO", _("Young Adult Fantasy")
        YADULTFIC = "YU", _("Young Adult Fiction")
        DEBUT = "DE", _("Debut Novel")
        NONFIC = "NO",_("Nonfiction")
        MEAUTO =  "ME", _("Memoir & Autobiography")
        HISBIO = "HB", _("History & Biography")
        HUMOR = "HU", _("Humor")
        ANY = "AN" , _("Any")

    title = models.CharField(max_length=100)
    pub_date = models.DateField()
    author = models.ManyToManyField('Author', related_name='books')
    pages = models.SmallIntegerField()
    category = models.CharField(max_length=2, choices=Category, default=Category.ANY)

    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=100)
    birth = models.DateField()

    def __str__(self):
        return self.name
