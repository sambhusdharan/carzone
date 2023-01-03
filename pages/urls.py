from . import views
from django.urls import path

urlpatterns = [
  path('',views.home,name='home'),
  path('about',views.about,name='About'),
  path('contact',views.contact,name='contact'),
  path('services',views.services,name='services'),
]
