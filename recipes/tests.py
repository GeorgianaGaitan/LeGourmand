from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from recipes.models import Recipe

class RecipeTests(TestCase):
    def setUp(self):
        #Set up user
        self.test_username = 'Test_User'
        self.test_pass = 'Test123!'
        self.user = User.objects.create_user(username=self.test_username, password=self.test_pass)

        #Set up recipes
        self.recipe_title = 'Test Recipe'
        self.recipe_description = 'Recipe for testing purposes'
        self.recipe_prep_time='30'
        self.recipe = Recipe.objects.create(
            title=self.recipe_title,
            description=self.recipe_description,
            prep_time=self.recipe_prep_time,
            user=self.user
        )

    def test_recipe_creation(self):
        self.assertEqual(Recipe.objects.count(), 1)
        self.assertEqual(self.recipe.title, self.recipe_title)
        self.assertEqual(self.recipe.user.username, self.test_username)

    def test_recipes_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.recipe_title)

    def test_recipe_detail_view(self):
        response = self.client.get(reverse('recipe_detail', args=[self.recipe.pk])) #get a pag
        self.assertEqual(response.status_code, 200) #pag incarcata corect
        self.assertContains(response, self.recipe_title)
        self.assertContains(response, self.recipe_description)

    def test_recipe_update(self):
        
        self.client.login(username=self.test_username, password=self.test_pass)
        response = self.client.post(reverse('recipe_update', args=[self.recipe.pk]), {
            'title': 'Updated Recipe',
            'description': 'Updated description',
            'prep_time': '45',
        })
        self.assertRedirects(response, reverse('recipe_detail', args=[self.recipe.pk]))
        self.recipe.refresh_from_db()
        self.assertEqual(self.recipe.title, 'Updated Recipe')
        self.assertEqual(self.recipe.description, 'Updated description')
        self.assertEqual(self.recipe.prep_time, '45')
