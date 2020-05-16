from django.urls import path
from . import views
urlpatterns = [
    path("table1/",views.bookview ,name="book"),
    path("table2/",views.bookview2 ,name="book"),
]