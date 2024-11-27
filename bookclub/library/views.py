from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.db import IntegrityError
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.views import generic
from django.urls import reverse
from .models import Book, Author, User, Genres
from .forms import NameForm, ContactForm, CreateUserFrom
from random import choice
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
    content["author_name"] = random_obj
    content["author_books"] = random_obj.books.all()
    if random_obj.books.count() > 4:
        content["author_over"] = True
    else:
        content["author_over"] = False

    # Randomly select genre
    pks = Genres.objects.values_list('pk', flat=True)
    random_pk = choice(pks)
    random_obj = Genres.objects.get(pk=random_pk)
    content["genre_name"] = random_obj
    content["genre_books"] = random_obj.books.all()[:10]
    if random_obj.books.count() > 4:
        content["genre_over"] = True
    else:
        content["genre_over"] = False
    
    
    return render(request, "library/browse.html", content)

def browse_book(request, book_id):
    content = {}
    if book_id:
        book = Book.objects.get(pk=book_id)
        print(book.genres.all())
        print(book.pub_date)
        content["book"] = book


    else:
        content["name"] = "home of books"
    
    return render(request, "library/book.html", content)
    
def browse_author(request, author_name=""):
    content = {}
    if author_name:
        content["name"] = author_name
    else:
        content["name"] = "home of authors"
    
    return render(request, "library/browse.html", content)

def browse_genre(request, genre_name=""):
    content = {}
    if genre_name:
        content["name"] = genre_name
    else:
        content["name"] = "home of genres"
    
    return render(request, "library/browse.html", content)