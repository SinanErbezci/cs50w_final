import csv
from datetime import datetime
from django.core.management.base import BaseCommand, CommandError
from library.models import Genres, Author, Series, Publisher, Book

class Command(BaseCommand):
    help = """
    ! Make sure you downloaded the csv file and added the file path of csv to the script. !
    ! Also make sure your database is empty. !
"""
    # Download the csv file from https://github.com/scostap/goodreads_bbe_dataset/tree/main/Best_Books_Ever_dataset
    # And add the file paths here.
    csv_path = "/Users/sinanerbezci/Desktop/git_repos/cs50w_final/bookclub/library/books_1.Best_Books_Ever.csv"

    def finding_genres(self, genres):
        genres_out = list()
        multiple_genres = genres.split(",")
        if len(multiple_genres) != 1:
            for genre in multiple_genres:
                gn, created = Genres.objects.get_or_create(name = genre)
                genres_out.append(gn)
                # if created:
                #     print("new genre created", genre)
        else:
            gn, created = Genres.objects.get_or_create(name = genres)
            genres_out.append(gn)
            # if created:
            #     print("new genre created", genre)
        
        return genres_out
    
    def finding_authors(self, authors):
        # Some of the data is lost with this method.
        # The reason for doing this is because getting additonal authors from this data is complicated.
        # illustrators, editors etc. are also included in authors column. 
        author = authors.split(",")[0]
        index = author.find("(")
        if index != -1:
            author_name = author[:index].strip()
        else:
            author_name = author.strip()

        aut, created = Author.objects.get_or_create(name = author_name)
        # if created:
        #     print("Author created", aut)

        return aut
    
    def finding_series(self, series):
        index = series.find("#")
        if index == -1:
            name = series.strip()
            number = None
        else:
            name = series[:index].strip()
            number = series[index+1:index+2]
        
        serie, _ = Series.objects.get_or_create(name = name)
        if not isinstance(number, int):
            number = None
        return serie, number
    
    def finding_publishers(self, publisher):
        publisher = publisher.strip()
        pb, created = Publisher.objects.get_or_create(name = publisher)
        # if created:
        #     print("publisher created ->", publisher)

        return pb
                
    def handle(self, *args, **options):
        with open(self.csv_path, "r") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                date = row["publishDate"]
                try:
                    d = datetime.strptime(date, "%m/%d/%y").date()
                except ValueError:
                    d = None

                try:
                    pages = int(row["pages"])
                except ValueError:
                    pages = None

                book_entry = Book(
                    title = row["title"],
                    description = row["description"],
                    pub_date = d,
                    pages = pages,
                    cover = row["coverImg"],
                )
                if row["publisher"]:
                    pb = self.finding_publishers(row["publisher"])
                    book_entry.publisher = pb
                if row["series"]:
                    series = self.finding_series(row["series"])
                    book_entry.series = series[0]
                    book_entry.series_num = series[1]
                
                book_entry.author = self.finding_authors(row["author"])
                book_entry.save()
                if row["genres"].strip("[]"):
                    gn_list = self.finding_genres(row["genres"].strip("[]"))
                    for gn in gn_list:
                        book_entry.genres.add(gn)