from django.urls import path,re_path
from .import views
from .views import contact_list

urlpatterns=[

       path('page2/', views.page2,name='page2'),
       path('createcontact/', views.createcontact,name='createcontact'),
       path('contact_list/', contact_list, name='contact_list'),





]