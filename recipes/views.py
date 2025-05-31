from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from .models import Recipe, Category
from .forms import RecipeForm
import random

class HomeView(ListView):
    model = Recipe
    template_name = 'recipes/home.html'
    context_object_name = 'recipes'
    
    def get_queryset(self):
        recipes = list(Recipe.objects.all())
        if len(recipes) > 5:
            return random.sample(recipes, 5)
        return recipes

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipes/recipe_detail.html'
    
class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipes/recipe_form.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.title)
        response = super().form_valid(form)
        # Save many-to-many relationships
        self.object.categories.set(form.cleaned_data['categories'])
        return response

class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipes/recipe_form.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super().form_valid(form)
        # Save many-to-many relationships
        self.object.categories.set(form.cleaned_data['categories'])
        return response
    
    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author

class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Recipe
    template_name = 'recipes/recipe_confirm_delete.html'
    success_url = reverse_lazy('home')
    
    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author

class CategoryRecipesView(ListView):
    model = Recipe
    template_name = 'recipes/category_recipes.html'
    context_object_name = 'recipes'
    
    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Recipe.objects.filter(categories=self.category)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context
