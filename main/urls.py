from django.urls import path, include
from .views import RecipeListCreateView,RecipeDetailView,IngredientListCreateView,IngredientDetailView,RatingListCreateView,RatingDetailView,CommentListCreateView,CommentDetailView

urlpatterns = [
    path('recipes/', RecipeListCreateView.as_view()),
    path('recipes/<int:pk>/', RecipeDetailView.as_view()),
    path('ingredients/', IngredientListCreateView.as_view()),
    path('ingredients/<int:pk>/', IngredientDetailView.as_view()),
    path('ratings/', RatingListCreateView.as_view()),
    path('ratings/<int:pk>/', RatingDetailView.as_view()),
    path('comments/', CommentListCreateView.as_view()),
    path('comments/<int:pk>/', CommentDetailView.as_view()),
]
