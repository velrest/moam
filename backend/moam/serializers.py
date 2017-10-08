from rest_framework import serializers
from moam.models import Book, Movie, Serie, Person

class BooksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ('name', 'state', 'api_id', 'image', 'page', 'author')

class MoviesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ('name', 'state', 'api_id', 'image', 'actors')

class SeriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Serie
        fields = ('name', 'state', 'api_id', 'image', 'actors', 'season', 'episode')

class PersonsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('name',)
