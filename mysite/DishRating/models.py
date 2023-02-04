from django.db import models

# Create your models here.


###############################################################
"""
    Class Users:

    Main purpose:
        Database handled for users sign up, sign in and logout
    
    Database Design: User1 as a Users Object
        User: [userName, userAccount(key), userPassword, userSignupDate]
        @  attr userName: String, charfeild with maximum length
        @  attr userAccount: Not duplicate, check before sign up
        @  attr userPassword: mix of everycharacter, min_length=6
        @  attr userSignupDate: trigger timezone api when sign up
"""
###############################################################
class Users(models.Model):
    userName = models.CharField(max_length=10)
    userAccount = models.CharField(max_length=30,primary_key=True)
    userPassword = models.CharField(max_length=30)
    userSignupDate = models.DateField()

    # Sign in button, collecting datas from the html and try
    # return 0 if success, -1 if failed
    def signIn(self, *args):
        pass

    # Sign up button, check id first. check length also. Do 
    # Error checking: try except
    # 
    def signUp(self, *args):
        pass

    # The things should do after user log in
    def afterIn(self, *args):
        pass

    def __str__(self):
        return self.userAccount

    ## TODO
    def getName(self):
        pass

    #TODO
    def getSignupDate(self):
        pass
    



###############################################################
"""
    Class Comments;

    Main Purpose: Stores comments from different people, used for
    display and other things

    Database Design: Comment1 as object
    Comment1: [comment, userAccount, pubDate]
    @  attr comment: CharField with max of 150 charcters
    @  attr userAccount: ForeignKey
    @  attr pubDate: DateTime obj store when the comment is pulished
"""
###############################################################
class Comments(models.Model):
    comment = models.CharField(max_length=150)
    userAccount = models.ForeignKey('Users',on_delete=models.SET('User Deleted the Account'))
    pubDate = models.DateTimeField()
    dishID = models.ForeignKey('DishRating.Dishes',on_delete=models.CASCADE)

    # Functions
    def __str__(self):
        return self.comment

    def getPubDate(self):
        pass

    def getDishID(self):
        pass




###############################################################
"""
    Class Dishes;

    Main Purpose: The dishes in Brandywine and Anteatery

    Database Design: Dish1
    @  attr dishName: CharField max_length = 30
    @  attr dishID: PRIMARY KEY
"""
###############################################################
class Dishes(models.Model):
    dishName = models.CharField(max_length = 30)
    dishID = models.IntegerField(primary_key=True)

    def __str__(self):
        return str(self.dishName)

    def getID(self):
        pass

    

    