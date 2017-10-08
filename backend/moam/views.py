from rest_framework import viewsets
from moam.models import Book, Person, Movie, Serie
from moam.serializers import PersonsSerializer, MoviesSerializer, SeriesSerializer, BooksSerializer

class BooksViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Mark to be viewed or edited.
    """
    queryset = Book.objects.all().order_by('-name')
    serializer_class = BooksSerializer

class MoviesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Mark to be viewed or edited.
    """
    queryset = Movie.objects.all().order_by('-name')
    serializer_class = MoviesSerializer

class SeriesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Mark to be viewed or edited.
    """
    queryset = Serie.objects.all().order_by('-name')
    serializer_class = SeriesSerializer

class PersonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Mark to be viewed or edited.
    """
    queryset = Person.objects.all().order_by('-name')
    serializer_class = PersonsSerializer
