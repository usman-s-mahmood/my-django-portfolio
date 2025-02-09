# created manually!
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='blog-index'),
    path("contact", views.contact, name='blog-contact')
]
