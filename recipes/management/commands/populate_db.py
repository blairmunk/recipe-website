from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.core.files.images import ImageFile
from recipes.models import Category, Recipe
import os

class Command(BaseCommand):
    help = 'Populates the database with sample data'

    def handle(self, *args, **options):
        # Create categories
        categories = [
            {'name': 'Breakfast', 'description': 'Morning meals to start your day'},
            {'name': 'Lunch', 'description': 'Midday meals to keep you going'},
            {'name': 'Dinner', 'description': 'Evening meals to end your day'},
            {'name': 'Dessert', 'description': 'Sweet treats to satisfy your cravings'},
            {'name': 'Vegetarian', 'description': 'Meatless dishes for vegetarians'}
        ]
        
        created_categories = []
        for category_data in categories:
            category, created = Category.objects.get_or_create(
                name=category_data['name'],
                defaults={
                    'slug': slugify(category_data['name']),
                    'description': category_data['description']
                }
            )
            created_categories.append(category)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created category: {category.name}'))
        
        # Create a superuser if none exists
        if not User.objects.filter(is_superuser=True).exists():
            user = User.objects.create_superuser('admin', 'admin@example.com', 'adminpassword')
            self.stdout.write(self.style.SUCCESS(f'Created superuser: {user.username}'))
        else:
            user = User.objects.filter(is_superuser=True).first()
        
        # Create recipes
        recipes = [
            {
                'title': 'Pancakes',
                'description': 'Fluffy pancakes with maple syrup',
                'preparation_steps': '1. Mix flour, eggs, and milk\n2. Cook on a hot griddle\n3. Serve with maple syrup',
                'preparation_time': 20,
                'categories': [created_categories[0], created_categories[3]],
            },
            {
                'title': 'Caesar Salad',
                'description': 'Classic Caesar salad with homemade dressing',
                'preparation_steps': '1. Wash and chop romaine lettuce\n2. Make dressing with garlic, anchovies, egg, lemon, oil\n3. Toss lettuce with dressing\n4. Add croutons and parmesan',
                'preparation_time': 15,
                'categories': [created_categories[1], created_categories[4]],
            },
            {
                'title': 'Spaghetti Bolognese',
                'description': 'Classic Italian pasta with meat sauce',
                'preparation_steps': '1. Cook onions, carrots, and celery\n2. Add ground beef and brown\n3. Add tomatoes and simmer\n4. Cook pasta and serve with sauce',
                'preparation_time': 45,
                'categories': [created_categories[2]],
            },
            {
                'title': 'Chocolate Cake',
                'description': 'Rich and moist chocolate cake',
                'preparation_steps': '1. Mix dry ingredients\n2. Add wet ingredients\n3. Bake at 350°F\n4. Cool and frost',
                'preparation_time': 60,
                'categories': [created_categories[3]],
            },
            {
                'title': 'Vegetable Stir Fry',
                'description': 'Quick and healthy vegetable stir fry',
                'preparation_steps': '1. Chop vegetables\n2. Heat oil in wok\n3. Stir-fry vegetables\n4. Add sauce and serve with rice',
                'preparation_time': 25,
                'categories': [created_categories[2], created_categories[4]],
            }
        ]
        
        for recipe_data in recipes:
            recipe, created = Recipe.objects.get_or_create(
                title=recipe_data['title'],
                defaults={
                    'slug': slugify(recipe_data['title']),
                    'description': recipe_data['description'],
                    'preparation_steps': recipe_data['preparation_steps'],
                    'preparation_time': recipe_data['preparation_time'],
                    'author': user,
                    # For simplicity, we're not adding images in this example
                }
            )
            
            if created:
                # Set categories for new recipes
                recipe.categories.set(recipe_data['categories'])
                self.stdout.write(self.style.SUCCESS(f'Created recipe: {recipe.title}'))
        
        self.stdout.write(self.style.SUCCESS('Database successfully populated!'))
