from django.urls import path
from . import views
urlpatterns = [
    
    path('home/',views.greet , name="welcome"),
    path("store/",views.items_here , name="itemsHere"),
]
