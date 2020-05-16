from . import views
from django.urls import path

urlpatterns = [
    
    path('',views.Greet,name="index"),
    path("help/",views.helpfun,name="func_help"),
]