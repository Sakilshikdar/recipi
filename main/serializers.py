from rest_framework import serializers
from .models import Main_Recipe, Recepi_Ingredient,Recepi_Comment,Recepi_Rating

class RecipeIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recepi_Ingredient
        fields = ['name']

class RecipeSerializer(serializers.ModelSerializer):
    ingredients = RecipeIngredientSerializer(many=True, read_only=True)

    class Meta:
        model = Main_Recipe
        fields = '__all__'

class RecipeRecipeRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recepi_Rating
        fields = '__all__'

class RecipeCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recepi_Comment
        fields = '__all__'
