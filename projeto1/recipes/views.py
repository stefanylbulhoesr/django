from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from utils.recipes.factory import make_recipe
from recipes.models import Recipe

def home(request):
    recipes = Recipe.objects.all().order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })

def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_detail_page' : True,
    })

