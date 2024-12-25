from django.urls import path
from . import views

urlpatterns = [
    # Landing Page
    path("", views.index, name="index"),

    # Account login
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("signup", views.signup, name="signup"),

    # Browse Section
    path("browse/", views.browse, name="browse"),
    path("browse/books/<int:book_id>", views.browse_book, name="book"),
    path("browse/genres/<int:genre_id>", views.browse_genre, name="genre"),
    path("browse/authors/<int:author_id>", views.browse_author, name="author"),

    # API Search

    path("search", views.search, name="search"),
]