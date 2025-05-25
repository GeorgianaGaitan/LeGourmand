from django.urls import include, path
from . import views

urlpatterns = [
    path("add/",views.create, name="recipe_create"),
    path('<int:pk>', views.recipe_detail, name='recipe_detail'),
    path('<int:pk>/delete/', views.recipe_delete, name='recipe_delete'),
    path('<int:pk>/edit/', views.recipe_update, name='recipe_update'),
]
