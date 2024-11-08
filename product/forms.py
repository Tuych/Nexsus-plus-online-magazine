from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'category', 'city', 'address', 'price', 'discount', 'condition']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control input-md', 'placeholder': 'Title'}),
            'category': forms.Select(attrs={'class': 'tg-select form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control input-md', 'placeholder': 'Ad your Price'}),
            'discount': forms.NumberInput(attrs={'class': 'form-control input-md', 'placeholder': 'Add discount'}),
            'description': forms.Textarea(attrs={'class': 'form-group md-3', 'placeholder': 'Add your description'}),
            'city': forms.Select(attrs={'class': 'tg-select form-control'}),
            'condition': forms.Select(attrs={'class': 'tg-select form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control input-md'}),

        }

