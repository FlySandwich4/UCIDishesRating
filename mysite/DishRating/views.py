from django.shortcuts import render
from django.http import HttpResponse
from .models import Comments, Users, Dishes

# Create your views here.

def mainpage(request):
    if(request.GET.get('mybtn')):
        print(2)
    return render(request,'DishRating/index.html')

def dishesPage(request):
    dishData = Dishes.objects.all()
    commentData = Comments.objects
    return render(request, 'DishRating/dishes.html',{
        'dishData':dishData,
        'commentData': commentData,
        'index': 0
    })

def introPage(request):
    return render(request, 'DishRating/intro.html')

def emberPage(request):
    dishData = Dishes.objects.filter(dishType="Ember")
    return render(request, 'DishRating/Ember.html',{
        'dishData': dishData
    })