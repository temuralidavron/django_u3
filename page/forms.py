from django import forms

from page.models import Category, Product


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

    def clean_name(self):
        name = self.cleaned_data['name']
        if Category.objects.filter(name=name).exists():
            raise forms.ValidationError('Category with this name already exists')
        return name


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category','name', 'price', 'description', 'image']


