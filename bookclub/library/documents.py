from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry

from .models import Book, Author, Genres, Publisher, Series

@registry.register_document
class BookDocument(Document):
    class Index:
        name = "books"
        settings = {"number_of_shards":1, "number_of_replicas":0}
    
    class Django:
        model = Book
        fields = ["title"]

@registry.register_document
class GenreDocument(Document):
    class Index:
        name = "genres"
        settings = {"number_of_shards":1, "number_of_replicas":0}
    
    class Django:
        model = Genres
        fields = ["name"]

@registry.register_document
class AuthorDocument(Document):
    class Index:
        name = "authors"
        settings = {"number_of_shards":1, "number_of_replicas":0}
    
    class Django:
        model = Author
        fields = ["name"]

@registry.register_document
class PublisherDocument(Document):
    class Index:
        name = "publishers"
        settings = {"number_of_shards":1, "number_of_replicas":0}
    
    class Django:
        model = Publisher
        fields = ["name"]

@registry.register_document
class SeriesDocument(Document):
    class Index:
        name = "series"
        settings = {"number_of_shards":1, "number_of_replicas":0}
    
    class Django:
        model = Series
        fields = ["name"]
