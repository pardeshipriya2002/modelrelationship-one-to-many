from app import views
from django.urls import path
# Create your models here.
urlpatterns=[
    path('home/',views.home,name='home')
]