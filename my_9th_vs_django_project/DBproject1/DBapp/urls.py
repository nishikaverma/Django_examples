from django.urls import path,include
from . import views
urlpatterns = [

    path("books/",views.showbookView, name="showbooks"),
]