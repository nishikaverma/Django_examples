from django.urls import path
from . import views


urlpatterns = [
    path("totalbooks/",views.addBooks, name="totalbooks"),
    #path("searchbooks/",views.searchFormView, name="formsearch"),
    path("search/", views.search, name="search"),
]

