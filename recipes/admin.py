from django.contrib import admin
from .models import Recipe, Category, RecipeCategory

class RecipeCategoryInline(admin.TabularInline):
    model = RecipeCategory
    extra = 1

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'preparation_time', 'created_at')
    list_filter = ('author', 'created_at')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [RecipeCategoryInline]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Category, CategoryAdmin)
