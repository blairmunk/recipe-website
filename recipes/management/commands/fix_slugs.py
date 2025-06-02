from django.core.management.base import BaseCommand
from recipes.models import Recipe, custom_slugify

class Command(BaseCommand):
    help = 'Fix empty or invalid slugs for recipes'

    def handle(self, *args, **options):
        recipes = Recipe.objects.all()
        fixed_count = 0
        
        for recipe in recipes:
            # Check if slug is empty or invalid
            if not recipe.slug or recipe.slug.strip('-') == '':
                original_slug = custom_slugify(recipe.title)
                new_slug = original_slug
                count = 1
                
                # Ensure uniqueness
                while Recipe.objects.filter(slug=new_slug).exclude(id=recipe.id).exists():
                    new_slug = f"{original_slug}-{count}"
                    count += 1
                
                recipe.slug = new_slug
                recipe.save()
                fixed_count += 1
                self.stdout.write(f"Fixed slug for recipe '{recipe.title}': '{new_slug}'")
        
        self.stdout.write(self.style.SUCCESS(f'Successfully fixed {fixed_count} recipe slugs'))