from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.showdatetime, name="date_time"),
]
