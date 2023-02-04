from django.urls import path

from . import views

urlpatterns = [
    path('', views.mainpage, name='sth'),
    path('dishes',views.dishesPage, name='dishes Page'),
]