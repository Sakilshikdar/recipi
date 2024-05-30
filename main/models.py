from django.db import models
from django.contrib.auth.models import User



class Recepi_Ingredient(models.Model):
    name = models.CharField(max_length=100)



class Main_Recipe(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Recepi_Ingredient)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Recepi_Rating(models.Model):
    recipe = models.ForeignKey(Main_Recipe, on_delete=models.CASCADE,)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class Recepi_Comment(models.Model):
    recipe = models.ForeignKey(Main_Recipe, on_delete=models.CASCADE,)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
