from django.urls import path,re_path
from .import views

urlpatterns=[

       path('page2/', views.page2,name='page2'),
       path('createcontact/', views.createcontact,name='createcontact'),




]