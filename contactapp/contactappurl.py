from django.urls import path,re_path
from .import views

from .views import startpage, create_contact, update_contact, delete_contact,contact_detail


urlpatterns = [
    path('startpage/', startpage, name='startpage'),
    path('create_contact/', create_contact, name='create_contact'),
    path('update_contact/<int:serial_number>/', update_contact, name='update_contact'),
    path('delete_contact/<int:serial_number>/', delete_contact, name='delete_contact'),
    path('contact_detail/<int:serial_number>/', contact_detail, name='contact_detail'),

]