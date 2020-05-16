from django.urls import path
from . import views


urlpatterns = [
    path( "books/",views.addBooksView , name="addBooks"),
    path( "getbooks/",views.getBooksViews , name="getBooks"),
]
