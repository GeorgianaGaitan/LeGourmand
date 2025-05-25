from django.shortcuts import render

from recipes.models import Recipe


def index(request):
    order_by = request.GET.get('orderBy', '-created_at')
    recipes = Recipe.objects.all().order_by(order_by)

    return render(request, 'recipe/list.html', {'recipes': recipes, 'order_by': order_by})
