from django.contrib import admin

from .models import Users, Comments, Dishes

admin.site.register(Users)
admin.site.register(Comments)
admin.site.register(Dishes)

# Register your models here.
