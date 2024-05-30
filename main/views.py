from rest_framework import generics
from .models import Main_Recipe, Recepi_Ingredient, Recepi_Comment, Recepi_Rating
from .serializers import RecipeIngredientSerializer,RecipeRecipeRatingSerializer,RecipeCommentSerializer,RecipeSerializer

class RecipeListCreateView(generics.ListCreateAPIView):
    queryset = Main_Recipe.objects.all()
    serializer_class = RecipeSerializer

class RecipeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Main_Recipe.objects.all()
    serializer_class = RecipeSerializer

class IngredientListCreateView(generics.ListCreateAPIView):
    queryset = Recepi_Ingredient.objects.all()
    serializer_class = RecipeIngredientSerializer

class IngredientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recepi_Ingredient.objects.all()
    serializer_class = RecipeIngredientSerializer

class RatingListCreateView(generics.ListCreateAPIView):
    queryset = Recepi_Rating.objects.all()
    serializer_class = RecipeRecipeRatingSerializer

class RatingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recepi_Rating.objects.all()
    serializer_class = RecipeRecipeRatingSerializer

class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Recepi_Comment.objects.all()
    serializer_class = RecipeCommentSerializer

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recepi_Comment.objects.all()
    serializer_class = RecipeCommentSerializer
