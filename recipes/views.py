from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required

from recipes.models import Recipe
from .forms import RecipeForm


def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipe/detail.html', {'recipe': recipe})

@login_required
def create(request):
    if request.method != 'POST':
        form = RecipeForm()
        return render(request, 'recipe/create.html', {'form': form})
   
    form = RecipeForm(request.POST)
    if form.is_valid():
        recipe = form.save(commit=False)
        recipe.user = request.user
        recipe.save()
        return redirect('home')
    
    
@login_required
def recipe_delete(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    recipe.delete()
    return redirect('home')


@login_required
def recipe_update(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)

    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = RecipeForm(instance=recipe)

    return render(request, 'recipe/edit.html', {'form': form, 'recipe': recipe, 'edit_mode': True})

