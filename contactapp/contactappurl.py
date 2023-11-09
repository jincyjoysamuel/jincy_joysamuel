from django.urls import path,re_path
from .import views
from .views import startpage
from .views import create_contact


urlpatterns=[

       path('startpage/', startpage, name='startpage'),
       path('create_contact/', create_contact, name='create_contact'),




]