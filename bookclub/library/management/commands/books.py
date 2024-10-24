import csv
from datetime import datetime
from django.core.management.base import BaseCommand, CommandError
from library.models import Genres, Author, Series, Publisher, Book

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

        elif func == "books":
            # entry = Book.objects.all()

            # if entry:
            #     raise CommandError("Books already exist")
            # else:
            #     self.stdout.write(self.style.SUCCESS("Book table is empty"))

            
            with open(self.csv_path, mode="r") as file:
                csv_reader = csv.DictReader(file)

                for row in csv_reader:
                    series_num = None
                    series_name = None
                    date = row["publishDate"]
                    try:
                        d = datetime.strptime(date, "%m/%d/%y").date()
                    except ValueError:
                        d = None
                    desc = row["description"]
                    cover = row["coverImg"]
                    try:
                        pages = int(row["pages"])
                    except ValueError:
                        pages = None
                    genre = row["genres"]
                    author = row["author"]
                    series = row["series"]
                    title = row["title"]
                    publisher = row["publisher"]

                    # publisher
                    p = Publisher.objects.get(name = publisher)
                    # series
                    if series:
                        series_index = series.find("#")
                        if series_index == -1:
                            series_name = series.strip()
                        else:
                            series_name = series[:series_index].strip()
                            try:
                                series_num = int(series[series_index+1:series_index+2].strip())
                            except ValueError:
                                series_num = None
                        s = Series.objects.get(name = series_name)
                    
                    bk = Book(
                        title = title, 
                        pages = pages,
                        cover = cover,
                        pub_date = d,
                        description = desc,
                        series_num = series_num,
                        series = s
                    )
                    bk.save()
                    # genres
                    try:
                        genre = genre.strip("[]")
                        if genre:
                            genres = genre.split(",")
                            if len(genres) > 1:
                                for x in genres:
                                    g = Genres.objects.get(name = x.strip(" '"))
                                    bk.genres.add(g)
                            else:
                                g = Genres.objects.get(name = genre.strip(" '"))
                                bk.genres.add(g)
                    except:
                        print("error",genre)    
                        # authors
                    try:
                        if author:
                            authors = author.split(",")
                            if len(authors) > 1:
                                for x in authors:
                                    index = x.find("(")
                                    if index != -1:
                                        x = x[:index].strip()
                                        a = Author.objects.get(name = x)
                                        bk.author.add(a)
                                    else:
                                        x = x.strip()
                                        if x.find(")") == -1:
                                            a = Author.objects.get(name = x)
                                            bk.author.add(a)
                            else:
                                index = author.find("(")
                                if index != -1:
                                    author = author[:index].strip()
                                    a  = Author.objects.get(name = author)
                                    bk.author.add(a)
                                else:
                                    a = Author.objects.get( name = author.strip())
                                    bk.author.add(a)
                    except:
                        print(author)

        else:
            raise CommandError("Wrong input")

# Rick Riordan (Goodreads Author), TK (Illustrator)
# Ai Mi, Anna Holmwood (Translator), 艾米
# Alistair MacLeod, پ, پژمان طهرانیان (Translator)
# M, Takami Nieda (Translator)
# Valentine, (Goodreads Author)
# Wataru Watari, 渡航, Ponkan⑧ (Illustrator), ぽんかん⑧ (イラスト)
# Alves/Mengistu, U
# error 'Manga', 'Shonen', 'Fantasy', 'Comics Manga', 'Comics', 'Graphic Novels', 'Action', 'Fiction', 'Young Adult', '漫画'
# Tan Jiu, 坛九
# Jan Edwards (Goodreads Author) (editor), Jenny Barber (editor), Anne Nicholls (contributor), Ian Whates (contributor), James Brogden (Goodreads Author) (contributor), Joyce Chng, (contributor), Zen Cho (Goodreads Author) (contributor), Adrian Tchaikovsky (Goodreads Author) (Contributor), more…
# Eiji Mikage, 御影 瑛路, 鉄雄 (イラスト)
# Eiji Mikage, 御影 瑛路, 鉄雄 (イラスト)
# Eiji Mikage, 御影 瑛路, 鉄雄 (イラスト)
# Eiji Mikage, 御影 瑛路, 鉄雄 (イラスト)