from . import views
from django.urls import path,include

urlpatterns = [
    
    path("showdatetime",views.ShowDateTimeView , name="showdatetime"),
    path("",views.homepageViews , name="homepage"),
    path("contact",views.contactpageViews , name="contactus"),
]