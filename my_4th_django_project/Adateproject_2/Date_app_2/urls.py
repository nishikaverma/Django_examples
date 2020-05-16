from django.urls import path
from . import views

urlpatterns = [
    path('date/',views.show_date,name="current_date"),
    path('',views.show_date,name="current_date"),
]