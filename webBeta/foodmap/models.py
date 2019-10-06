from django.db import models
from django.urls import reverse
# Create your models here.
class FoodType(models.Model):


    type = models.CharField(max_length=20, help_text='Enter food type')

    class Meta:
        ordering = ['-type']

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.type)])

    def __str__(self):
        return self.type

class Food(models.Model):

    name = models.CharField(max_length=20,help_text='Enter food name')
    type = models.ForeignKey('FoodType',on_delete=models.SET_NULL,null=True)
    summary = models.TextField(max_length=1000,help_text='Enter your opinion',blank=True)
    score = models.SmallIntegerField(max_length=10,blank=True)
    restaurant = models.ForeignKey('Restaurant')

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.name