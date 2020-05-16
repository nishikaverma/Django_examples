from . import views
from django.urls import path,include

urlpatterns = [
    path('',views.homePageviews , name='home' ),
    path('home/',views.homePageviews , name='home' ),
    path('addbooks/', views.takeBooksrecord, name='addbooks'),
    path('addbookstodb/', views.addBooksToDB, name='addbookstodb'),
    path('showbooks/',views.showBooks , name='showbooks'),


]
