from django.db import models

class Media(models.Model):
    name = models.TextField()
    state = models.CharField(max_length=11)
    api_id = models.IntegerField()
    image = models.ImageField()

    class Meta:
        abstract = True

class Person(models.Model):
    name = models.CharField(max_length=250)

class Book(Media):
    page = models.IntegerField(default=1)
    author = models.ManyToManyField(Person)
    
class Movie(Media):
    actors = models.ManyToManyField(Person)

class Serie(Movie):
    season = models.IntegerField(default=1)
    episode = models.IntegerField(default=1)
