from django.urls import path
from . import views
urlpatterns = [

    path('',views.home),
    path('home/',views.home ,name='home'),
    path('display',views.read , name='display'),
    path('create',views.createit, name='createit'),
    path('update',views.updateit, name='updateit'),
    path('deleteall',views.deleteall, name='deleteall'),
    path('deleteone',views.deleteit, name='deleteit'),
    
    path('create_it_form/',views.create, name='create'),
    
    path('details/',views.searchDetails, name='searchDetails'),
    path('details_result/',views.update, name='update'),
    path('delete_record/',views.deleteone, name='deleteone'),
    
]
