from django.urls import path,include
from . import views

urlpatterns = [ path('', views.greet , name= 'index'),
path("showDate/",views.currentDate, name="index"),
path("showTime/",views.currentTime, name="index"),
path("showKeys/",views.key_values, name="k_v"),
 ]