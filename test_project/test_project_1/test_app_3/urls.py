from django.urls import path
from . import views

urlpatterns=[path("",views.complainFun,name="func_complain")


]