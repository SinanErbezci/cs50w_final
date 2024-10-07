from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from .models import Book,Author
from .forms import NameForm, ContactForm
# Create your views here.

class IndexView(generic.ListView):
    template_name = "library/index.html"
    context_object_name = "latest_books_added"

    def get_queryset(self):
        """Return last added 5 books """
        return Book.objects.all()[:5]

class DetailView(generic.DetailView):
    model = Book
    template_name = "library/book.html"


def index(request):
    hello = "hello, world"
    books = Book.objects.all()
    output = {"hello" : hello, "books":books}
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
