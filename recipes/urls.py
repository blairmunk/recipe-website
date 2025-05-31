from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('recipe/new/', views.RecipeCreateView.as_view(), name='recipe-create'),
    path('recipe/<slug:slug>/', views.RecipeDetailView.as_view(), name='recipe-detail'),
    path('recipe/<slug:slug>/update/', views.RecipeUpdateView.as_view(), name='recipe-update'),
    path('recipe/<slug:slug>/delete/', views.RecipeDeleteView.as_view(), name='recipe-delete'),
    path('category/<slug:slug>/', views.CategoryRecipesView.as_view(), name='category-recipes'),
]
