from django.shortcuts import render
from django.http import HttpResponse
from .models import Comments, Users, Dishes
from django.utils import timezone
from django.http import HttpResponseRedirect
# views.py
from django.shortcuts import redirect

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
    # Mar/9/2023 changed to intro_v2
    return render(request, 'DishRating/intro_v2.html')

def emberPage(request):
    dishData = Dishes.objects.filter(dishType="Ember")
    return render(request, 'DishRating/Ember.html',{
        'dishData': dishData
    })


def grubbPage(request):
    dishData = Dishes.objects.filter(dishType="Grubb")
    return render(request, 'DishRating/Grubb.html',{
        'dishData': dishData
    })

def pizzaPage(request):
    dishData = Dishes.objects.filter(dishType="Pizza")
    return render(request, 'DishRating/Pizza.html',{
        'dishData': dishData
    })

def soupsPage(request):
    dishData = Dishes.objects.filter(dishType="Soups")
    return render(request, 'DishRating/Soups.html',{
        'dishData': dishData
    })

def veganPage(request):
    dishData = Dishes.objects.filter(dishType="Vegan")
    return render(request, 'DishRating/Vegan.html',{
        'dishData': dishData
    })

def bakeryPage(request):
    dishData = Dishes.objects.filter(dishType="Bakery")
    return render(request, 'DishRating/Bakery.html',{
        'dishData': dishData
    })

def commentPage(request, urlDishID):
    if request.method == 'POST':
        postDic = request.POST
        print(postDic["comment"])
        theUser = Users.objects.get(userAccount="Anonymous")
        theDish = Dishes.objects.get(dishID=urlDishID)
        Comments(comment=postDic["comment"],userAccount=theUser,
                 pubDate=timezone.now(),
                 dishID=theDish).save()
        return HttpResponseRedirect(request.path_info)
    dishData = Dishes.objects.get(dishID=urlDishID)
    print(dishData)
    commentData = Comments.objects.filter(dishID=urlDishID)
    comUsrData = []
    for each in commentData:
        comUsrData.append([each,Users.objects.get(userAccount=each.userAccount)])
    print("comment")
    print(commentData)

    return render(request,'DishRating/comment.html',{
        'dishData':dishData,
        'comUsrData':comUsrData,
    })