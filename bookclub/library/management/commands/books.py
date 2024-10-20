from django.core.management.base import BaseCommand, CommandError
import csv
from library.models import Genres, Author, Series, Publisher

class Command(BaseCommand):
    help = """
        Applications for database. Database has to be empty.
        Creating genres: "genres",
        Creating publishers: "publishers",
        Creating series: "series",
        !Before creating make sure you created all the other tables!
        Creating books: "books"
"""
    csv_path = "/Users/sinanerbezci/Desktop/git_repos/cs50w_final/bookclub/library/books_modified.csv"
    def add_arguments(self, parser):
        parser.add_argument("func", type=str, help="Functionality")

    def finding_genres(self):
        with open(self.csv_path, mode = 'r') as file:
            csv_reader = csv.DictReader(file)
            genres_set = set()
            for row in csv_reader:
                row = row["genres"].strip("[]")
                multiple_genres = row.split(",")
                if len(multiple_genres) != 1:
                    for genre in multiple_genres:
                        genres_set.add(genre.strip(" '"))
                else:
                    genres_set.add(row.strip(" '"))

        genres_list = list(genres_set)
        genres_list.sort()
        return genres_list[1:-1]
    
    def finding_authors(self):
        with open(self.csv_path, mode = 'r') as file:
            csv_reader = csv.DictReader(file)
            authors_set = set()
            for row in csv_reader:
                row = row["author"].split(",")
                if len(row) > 1:
                    for author in row:
                        index = author.find("(")
                        if index != -1:
                            a = author[:index].strip()
                            if len(a) > 2:
                                authors_set.add(a)
                        else:
                            c = author.strip()
                            if c.find(")") == -1:
                                if len(c) > 2:
                                    authors_set.add(c)
                else:
                    index = row[0].find("(")
                    if index != -1:
                        b = row[0][:index].strip()
                        authors_set.add(b)
                    else:
                        b = row[0].strip()
                        authors_set.add(b)

        authors_list = list(authors_set)
        authors_list.sort()
        return authors_list
    
    def finding_series(self):
        with open(self.csv_path, mode="r") as file:
            csv_reader = csv.DictReader(file)
            genres_dict = dict()
            
            for row in csv_reader:
                serie = row["series"]
                if serie:
                    index = serie.find("#")
                    if index == -1:
                        name = serie.strip()
                    else:
                        name = serie[:index].strip()
                    current = genres_dict.get(name)
                    if current:
                        genres_dict[name] = current + 1
                    else:
                        genres_dict[name] =  1

        return dict(sorted(genres_dict.items()))
    
    def finding_publishers(self):
        with open(self.csv_path, mode="r") as file:
            csv_reader = csv.DictReader(file)
            publishers_set = set()
        
            for row in csv_reader:
                publisher = row["publisher"].strip()
                publishers_set.add(publisher)

        publishers_list = list(publishers_set)
        publishers_list.sort()

        return publishers_list
                
    def handle(self, *args, **options):
        func = options["func"]
        if func == "genres":
            # Check if genres table is empty
            entry = Genres.objects.all()
            
            if entry:
                raise CommandError("Genres already exist.")
            else:
                self.stdout.write(self.style.SUCCESS("Genres table is empty"))

            self.stdout.write("Creating genres")
            genres = self.finding_genres()            
            
            for genre in genres:
                p = Genres.objects.create(name = genre)
            
            self.stdout.write(self.style.SUCCESS("Genres are created"))
        
        elif func == "authors":
            entry = Author.objects.all()

            if entry:
                raise CommandError("Authors already exist.")
            else:
                self.stdout.write(self.style.SUCCESS("Authors table is empty"))
            
            self.stdout.write("Creating authors")
            authors = self.finding_authors()

            for author in authors:
                a = Author.objects.create(name = author)
        
        elif func == "series":
            entry = Series.objects.all()
            if entry:
                raise CommandError("Series already exist")
            else:
                self.stdout.write(self.style.SUCCESS("Series table is empty"))
            
            self.stdout.write("Creating series")
            series = self.finding_series()

            for name, number in series.items():
                s = Series.objects.create(
                    name = name,
                    number = number
                )

        elif func == "publishers":
            entry = Publisher.objects.all()

            if entry:
                raise CommandError("Publishers already exist")
            else:
                self.stdout.write(self.style.SUCCESS("Publisher table is empty"))
            
            self.stdout.write("Creating publishers")
            publishers = self.finding_publishers()

            for publisher in publishers:
                p = Publisher.objects.create(name=publisher)

        else:
            raise CommandError("Wrong input")

# def finding_authors():
#     with open('goodreads_data.csv', mode = 'r') as file:
#         csv_reader = csv.DictReader(file)
#         author_set = set()
#         for row in csv_reader:
#             author_set.add(row["Author"].strip())
        
#         return author_set


# def max_desc():
#     with open('books_modified.csv', mode = 'r') as file:
#         csv_reader = csv.DictReader(file)
#         max_len = 10000
#         for row in csv_reader:
#             current_len = len(row["description"])
#             if current_len > max_len:
#                 print(row["title"])

#         # max_len = 8947


        # genres = finding_genres()
        # for genre in genres:
        #     Genres.objects.create(
        #         name = genre
        #     )

    # genre_set = finding_genres()
    # genre_list = list(genre_set)
    # genre_list.sort()
    # genre_len = [len(item) for item in genre_list]
    # genre_len.sort()
    # print(genre_len)
    # print(len(genre_list))
    # author_set = finding_authors()
    # authors_list = list(author_set)
    # authors_list.sort()
    # print(authors_list)

    # with open('books_modified.csv', mode = 'r') as file:
    #     csv_reader = csv.DictReader(file)
    #     genres_set = set()
    #     for row in csv_reader:
    #         row = row["genres"].strip("[]")
    #         multiple_genres = row.split(",")
    #         if len(multiple_genres) != 1:
    #             for genre in multiple_genres:
    #                 genres_set.add(genre.strip(" '"))
    #         else:
    #             genres_set.add(row.strip(" '"))

    # genres_list = list(genres_set)
    # genres_list.sort()
    # print(genres_list[1:-1])
    # print("len", len(genres_list[1:-1]))

    # with open('books.csv', mode = 'r') as file:
    #     csv_reader = csv.DictReader(file)
    #     authors_set = set()
    #     for row in csv_reader:
    #         row = row["author"].split(",")
    #         if len(row) > 1:
    #             for author in row:
    #                 authors_set.add(author.strip())
    #         else:
    #             row[0].strip()

    # authors_list = list(authors_set)
    # authors_list.sort()
    # print(len(authors_list))

    # max_desc()