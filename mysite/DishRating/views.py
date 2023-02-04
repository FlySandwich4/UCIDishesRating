from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def mainpage(request):
    if(request.GET.get('mybtn')):
        print(2)
    return render(request,'DishRating/index.html')