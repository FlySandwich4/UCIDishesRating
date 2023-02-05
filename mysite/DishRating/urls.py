from django.urls import path

from . import views

app_name = 'DishRating'

urlpatterns = [
    path('', views.introPage, name='Home'),
    path('dishes',views.dishesPage, name='dishes Page'),
    path('ember',views.emberPage, name="ember"),
    path('dishes/<int:urlDishID>',views.commentPage, name="comment"),
    path('grubb',views.grubbPage, name="grubb"),
    path('pizza',views.pizzaPage, name="pizza"),
    path('soups',views.soupsPage, name="soups"),
    path('vegan',views.veganPage, name="vegan"),
    path('bakery',views.bakeryPage, name="bakery"),
]