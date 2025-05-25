from django import forms
from recipes.models import Recipe


class RecipeForm(forms.ModelForm):
    #Prep time displayed as number field
    prep_time = forms.IntegerField(
        min_value=1,
        max_value=999,
        widget=forms.NumberInput(attrs={
            'class': 'form-control'
        }),
        label='Duration (minutes)'
    )
    
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'prep_time']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'rows': 5,
                'class': 'form-control'
            }),
        }
        
    #Save prep_time as string
    def clean_prep_time(self):
        value = self.cleaned_data['prep_time']
        return str(value)