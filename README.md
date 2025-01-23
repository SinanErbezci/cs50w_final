# Bookclub - CS50W Final Project
#### Video Demo: 
#### Description: The book platform where you can find the books you searched, create your lists, and write your book reviews.

### 1. Overview of the Project
Bookclub is a platform where users can search over 50000 books, genres, or authors they want to find. Additionally, the users can follow other users, write reviews, and rate the books they've read. Finally, users can create their lists and add the books to their lists.

The database is taken from Goodreads and implemented into Django by creating a custom django-admin command. This script easily imports a CSV file (1) and creates books, genres, and authors at the same time. Relational links are also established during this process.

Searching is one of the main parts of the project. To achieve great performance Elasticsearch (2) is used. Elasticsearch offers near real-time performance. This is very useful for instant search where users can search on any page and get results within seconds. Also, there is a specific page where users can find all the results corresponding to their search input.

The browse page shows the last added books, books from one random genre and one random author. Users can find new books, and the other browse pages are specific to a book, genre, and author. On the book page, users can write reviews and read other users' reviews. On the author and genre pages, users can find books specific to that author or genre.

The profile page shows users' reviews, the people they follow, and the lists that they have created. Also, they can look at others' profiles too. 

### 2. Distinctiveness and Complexity

This project is quite distinctive from other projects of the course. One of the main pieces of the project is searching feauture. It includes additional parts compared to projects of the course such as elastic-search and instant search applications via javascript. Complexity-wise, it is moderately complicated. The database is quite large which includes more than 80k entries. Importing these data into Django and searching through it, is a complex process. Also on the front end, using Bootstrap's advanced features and javascript implementations makes rather a complex task.

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


