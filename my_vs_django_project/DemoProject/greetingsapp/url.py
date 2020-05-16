# APPLICATION LEVEL URL
from django.urls import path,include
from . import views

urlpatterns = [ path('sca/', views.homepageViews , name= 'index'),
 ]