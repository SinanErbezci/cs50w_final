# Bookclub - CS50W Final Project
#### Video Demo: https://youtu.be/kAA-FCxAqx8https
#### Description: The book platform where you can find the books you searched, create your lists, and write your book reviews.

### 1. Overview of the Project
Bookclub is a platform where users can search over 50000 books, genres, or authors they want to find. Additionally, the users can follow other users, write reviews, and rate the books they've read. Finally, users can create their lists and add the books to their lists.

The database is taken from Goodreads and implemented into Django by creating a custom django-admin command. This script easily imports a CSV file (1) and creates books, genres, and authors at the same time. Relational links are also established during this process.

Searching is one of the main parts of the project. To achieve great performance Elasticsearch (2) is used. Elasticsearch offers near real-time performance. This is very useful for instant search where users can search on any page and get results within seconds. Also, there is a specific page where users can find all the results corresponding to their search input.

The browse page shows the last added books, books from one random genre and one random author. Users can find new books, and the other browse pages are specific to a book, genre, and author. On the book page, users can write reviews and read other users' reviews. On the author and genre pages, users can find books specific to that author or genre.

The profile page shows users' reviews, the people they follow, and the lists that they have created. Also, they can look at others' profiles too. 

### 2. Distinctiveness and Complexity

This project is quite distinctive from other projects of the course with following aspects:
- It uses advance feautures of Bootstrap. Such as modals, popovers, grid system, offcanvas, custom colors with Sass and more. This features are both used in HTML and JS(especially popovers and modals).
- One of the main part of this project is searching feature. It uses ElasticSearch to get very quick results. To get ElasticSearch work with Django and the database is quite complex task.
- Database includes over 80k entries from GoodReads. Importing these data to Django and creating relations between books, author and genres are done by custom Django-admin command.
- Front-end of the project is very responsive. Based on view-width, the layout of the books change and some parts can appear/disappear.

### 3. Files and Directories

- cs50w-final 
    - bookclub
        - db.sqlite3
            > It can be downloaded from [Resources-5](#resources)
        - bookclub
            - settings.py
                > Settings of the Django Project. ElasticSearch url is given with username and password. Time-zone and other some options are changed.
            - ...
        - library
            - management/commands
                - books.py
                    > Custom django-admin command. It reads data from BestBooksDataset and creates books, genres and authors. It starts reading books and looks as if genre and author exists in the database. If it's not, it creates them and adds corresponding relation. Also it makes data transformation like datetime, string striping etc.
            - static/library
                - images
                    > All the images that used in the project. Icons, pictures etc.
                - sass
                - main.min.css
                    > Custom bootstrap module is used. Primary and border color is changed.
                - BookClub.js
                    > Defines InstantSearch class. This class performs the search, populate results and does additional features.
                - browse.js
                    > JS module used in the browse/book page. It appear/disappear "Read More" button, fills the stars of reviews, submits the review form and also does the all popover features of "Adding to list" button.
                - follow.js
                    > JS module used in the profile page. It makes API call to follow/unfollow users.
                - mainSearch.js
                    > JS module used in the search page. It selects/deselects the book,genre or author options.
                - profile.js
                    > JS module used in the profile page. It fills the reviews stars, fills the modal and makes the API all to get books in a list and fills the modal with those books.
                - search.js
                    > It just initiate the InstantSearch class from BookClub.js.
                - style.css
                    > CSS file specifices coloring, sizing, some utility functionalities and etc.
            - documents.py
                > It is used for creating ElasticSearch indexes from the Django models. It is only one time executed after that the indexes are created and can be used.
            - templates/library
                > All the html files of the projects.
            - forms.py
                > Creates custom form for the Sign Up page. Uses basic UserCreationForm of Django.
            - models.py
                > Django models includes User,Book,Author,Genre, Lists and etc.
            - views.py
                > All the view function of the pages and API functions.
            - urls.py 
                > All the page urls and API urls.
            - ...
    - .gitignore
        > Some of the files are ignored to decrease the size of git rep. Such as db.sqlite3, elasticsearch files.
    - elastic-start-local
        > It can be downloaded from [Resources-6](#resources)
        - .env
        - docker-compose.yml
            > Docker configurations for ElasticSearch. It specifies which feautures are used and get the user data from .env file. 
        - start.sh
        - stop.sh
        - uninstall.sh
            > Scripts for start,stop and uninstall of ElasticSearch.
    - README.md
    - requirements.txt
### 3. Database Integration

As stated before, the database is derived from the Best Books Ever dataset (1) which includes over 50k records from Goodreads. This dataset includes many columns where it's not useful for the project. So for the decreasing size of the project, these columns are deleted (such as price, characters, etc.). To make this process automated custom command is created. It is called **books.py** located in bookclub/library/management/commands. This script imports the data from a CSV file and starts reading books from the dataset. Some data conversions are made such as turning date into datetime etc. Also, authors and genres are automatically created through reading data from CSV. Firstly, it looks if the author and genres exist in the database. If not, it creates the new objects and adds the relationship between the objects.

### 4. Searching Feature
To implement Elasticsearch on a Django project, there are some useful Python libraries (2). Elasticsearch works as a server. To fill data into Elasticsearch, indexes should be created. **documents.py** file creates these indexes. This file configures documents which correspond to Django models. The main documents are derived from Books, Genres, and authors. Only the name field is used therefore, the description of a book is not considered during the search.

After documents are created, elastic-search is started. Elasticsearch works as a server. The client gives a query with some parameters to a URL (localhost:9200) and elastic-search gives the result as JSON. This URL should be set in **settings.py** so that Django knows which URL to look for. Also after the initialization of elastic-search, it gives username and password. These are also should be provided in **settings.py**.

There are two types of searching in this project. The first one is the instant search where users enter some text on the search bar which is located on the navigation bar. Javascript detects the user input and fetches a call to the elastic-search URL. Then modifies the output and shows below the search bar (4). Additionally, some **fuzziness** is included in the search. So even if the user mistypes some words, it shows a similar result.

The second one is the basic search (**./search.html**). The user selects a book, author, or genre. The page gives the paginated results for the query.
### 5. Content and Desing of the Pages
All the icons and images of the project are created with Microsoft Copilot. Also, the color scheme is derived from Copilot. Bootstrap icons and bootstrap framework are also used.

Starting with the homepage(**index.html**), it's a landing page for new users. On the top, there is a navigation bar. The Bookclub icon is on the left side of the bar. The search bar is located in the middle. Login and register links are on the right side. After the user is authenticated, login and register links are replaced by profile, browse, search, and logout buttons. The landing page shows some visuals that represent the app and sign-up and login buttons.

On the browse page(**/browse/**) recently added 4 books are shown on the top. These are the last added books that have the highest IDs on the book models. On the second row, it shows books from a randomly selected author. Also on the third, it shows books from randomly selected genres. Books are represented in card format. The top is the book image with fixed dimensions, below that is the name of the book which is limited to 2 rows, and finally the name of the author. Book name and author are also links. Also, it is mobile-responsive. On bigger screens it shows 4 cards, on medium it shows 2 and on mobile it shows 1. Users can scroll horizontally to look at other cards.

The book page (**/browse/book/**) gives details about the book which are description, genres, author, publisher and publish date. Users can write reviews, see their reviews, and also look at others' reviews. When you click the review, the content of the reviews shows up in the **bootstrap modal**. Additionally, user can add the book to their existing list or create a new list. And they can remove it from the list if it's in a list. Also, if the description exceeds 7 lines, the overflow becomes hidden, and **Read More** appears. When a user clicks on the button the description expands to show all of the description. This is checked every time the window is resized so that the button can appear and disappear.

The genre page (**/browse/genre**) and author page (**browse/author**) show books specific to that part. It is also paginated and shows a maximum of 4 books a page.

The profile page (**/profile**) shows users' reviews, the people they follow, and their lists. When a user clicks on a list, it makes an API call to get which books are in the list and it shows in a bootstrap modal.

### 6. Running the Application
Git commit does not contain database and elastic-search because it exceeds the storage limit. Database can be downloaded from [Resources-1](#resources). After downloading the database it should be transfered to django by using **books.py**.

Secondly, elastic-search should be installed from [Resources-2](#resources). And the indexes should be created by using Django Elasticsearch DSL and **documents.py**.

Finally, python packages can be installed from requirements.txt.
### Resources
(1) -> Best Books Ever Dataset - https://zenodo.org/records/4265096

(2) -> Elasticsearch - https://www.elastic.co/guide/en/elasticsearch/reference/7.17/getting-started.html - https://www.youtube.com/watch?v=lKanpfkhxv0

(3) -> Instant search bar - https://www.youtube.com/watch?v=M3PbUwgEecU&list=LL&index=7

(4) -> Django Elasticsearch DSL - https://django-elasticsearch-dsl.readthedocs.io/en/latest/

(5) -> Database - https://www.mediafire.com/file/g9fm32z7lgvs76h/db.sqlite3/file 

(6) -> docker file for elasticsearch - https://www.mediafire.com/file/ycermit5ctz2qvv/elastic.zip/file

