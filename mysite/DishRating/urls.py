from django.urls import path

from . import views

urlpatterns = [
    path('', views.introPage, name='sth'),
    path('dishes',views.dishesPage, name='dishes Page'),
    path('ember',views.emberPage, name="ember")
]