from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = 'categories'
        
    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('category-recipes', kwargs={'slug': self.slug})

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    preparation_steps = models.TextField()
    preparation_time = models.IntegerField(help_text="Preparation time in minutes")
    image = models.ImageField(upload_to='recipe_images', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, through='RecipeCategory')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('recipe-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        # Generate a slug if one doesn't exist
        if not self.slug:
            self.slug = slugify(self.title)
            
            # Ensure uniqueness
            original_slug = self.slug
            count = 1
            while Recipe.objects.filter(slug=self.slug).exists():
                self.slug = f"{original_slug}-{count}"
                count += 1
                
        super().save(*args, **kwargs)

class RecipeCategory(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = 'recipe categories'
        unique_together = ('recipe', 'category')
        
    def __str__(self):
        return f"{self.recipe.title} - {self.category.name}"
