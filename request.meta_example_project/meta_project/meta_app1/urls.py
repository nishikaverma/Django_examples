from django.urls import path,include
from . import views

urlpatterns = [
    path("show/",views.display_meta, name="displayMeta"),
    path("showall/",views.display_all_headders, name="displayall"),
    ]