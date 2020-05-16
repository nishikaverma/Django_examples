from django.urls import path
from. import views
urlpatterns = [
    path('',views.homePage , name="homePage"),
    path("enternos/",views.displayForm , name="form"),
    path("add/", views.addnos,name='add'),
]
