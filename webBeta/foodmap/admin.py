from django.contrib import admin
from  .models import Food,FoodType

# Register your models here.
admin.site.register(FoodType)
admin.site.register(Food)