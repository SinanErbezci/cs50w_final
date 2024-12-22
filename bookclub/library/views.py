from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.views import generic
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from .models import Book, Author, User, Genres, Review
from .forms import NameForm, ContactForm, CreateUserFrom
from random import choice
from decimal import Decimal

def index(request):
    hello = "hello, world"
    output = {"hello" : hello}
    return render(request, "library/index.html",output)

def create_book(request):
    if request.method == "POST":
        form =  ContactForm(request.POST)
        if form.is_valid():
            print("sender",form.cleaned_data["sender"])
        return HttpResponseRedirect(reverse("index"))
    else:
        form = ContactForm()

    return render(request, "library/create_book.html", {"form" : form})


# User views
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("index")
            # username = form.cleaned_data["username"]
            # password = form.cleaned_data["password"]
            
            # user = authenticate(request, username=username, password=password)   

            # if user is not None:
            #     login(request, user)
            #     print("a")
            #     return redirect("index")
            # else:
            #     print("b")
    else:
        form = AuthenticationForm()

    return render(request, "library/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def signup(request):
    if request.method == "POST":
        form = CreateUserFrom(request.POST)
        if form.is_valid():
            print("valid")
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            form.save()
            new_user = authenticate(username=username, password=password)
            if new_user is not None:
                login(request,new_user)
                return redirect("index")
    else:  
        form = CreateUserFrom()

    return render(request, "library/signup.html", {"form": form})

def browse(request):
    content = {}
    # Last added books
    content["recently"] = Book.objects.all().order_by("-pk")[:4]

    # Randomly select author
    pks = Author.objects.values_list('pk', flat=True)
    random_pk = choice(pks)
    random_obj = Author.objects.get(pk=random_pk)
    content["author"] = random_obj
    content["author_books"] = random_obj.books.all()
    if random_obj.books.count() > 4:
        content["author_over"] = True
    else:
        content["author_over"] = False

    # Randomly select genre
    pks = Genres.objects.values_list('pk', flat=True)
    random_pk = choice(pks)
    random_obj = Genres.objects.get(pk=random_pk)
    content["genre"] = random_obj
    content["genre_books"] = random_obj.books.all()[:10]
    if random_obj.books.count() > 4:
        content["genre_over"] = True
    else:
        content["genre_over"] = False
    
    
    return render(request, "library/browse.html", content)

def browse_book(request, book_id):

    if request.method == "POST":
        text = request.POST["text"]
        rating = request.POST["rating"]
        rating = int(rating)

        user_review = Review.objects.filter(book_id_id = book_id, user_id_id = request.user.id)
        if user_review:
            print("user has review")
            return redirect("index")
        review = Review(book_id_id=book_id, user_id_id=request.user.id, rating=rating, text=text)
        review.save()
        messages.success(request, "You've succesfully submitted your review.")
        
        # Update Ratings
        book = Book.objects.get(pk=book_id)
        num_ratings = book.num_ratings
        book_rating = book.rating
        new_total = num_ratings * book_rating + rating
        new_rating =  Decimal(new_total/(num_ratings + 1)).quantize(Decimal("1.0"))
        book.num_ratings = num_ratings + 1
        book.rating = new_rating
        book.save()

    
    content = {}
    if book_id:
        if request.user.is_authenticated:
            user_review = Review.objects.filter(book_id_id = book_id, user_id_id = request.user.id)
            if user_review:
                content["user_review"] = user_review[0]
            else:
                content["user_review"] = None

        book = Book.objects.get(pk=book_id)
        content["book"] = book
        reviews = Review.objects.filter(book_id = book).exclude(user_id_id = request.user.id)
        content["reviews"] = reviews


    else:
        content["name"] = "home of books"
    
    return render(request, "library/browse_book.html", content)
    
def browse_author(request, author_id):
    content = {}
    try:
        author = Author.objects.get(pk=author_id)
    except ObjectDoesNotExist:
        return redirect("index")

    content["author"] = author
    print(author)
    books = author.books.all()
    content["books"] = books
    if books.count() > 4:
        content["over"] = True
    else:
        content["over"] = False
    return render(request, "library/browse_author.html", content)

def browse_genre(request, genre_id):
    content = {}
    try:
        genre = Genres.objects.get(pk = genre_id)
        content["name"] = genre.name
    except ObjectDoesNotExist:
        return redirect("index")

    paginator = Paginator(genre.books.all(), 4)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    content["page_obj"] = page_obj

    
    return render(request, "library/browse_genre.html", content)
