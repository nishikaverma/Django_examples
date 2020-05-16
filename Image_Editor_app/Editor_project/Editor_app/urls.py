from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage, name="homepage"),
    path('ChoosenImage/',views.uploadImg, name='uploadImg'), # when submit button (upload ) is clicled then the value given to action attribute i.e. the url's name is searched here.
    ]
