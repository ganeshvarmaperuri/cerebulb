from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['email','first_name','last_name','password1', 'password2']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name', 'category_code']


class ProductForm(forms.ModelForm):
    product_mfg_date = forms.DateField()
    category = forms.ModelChoiceField(queryset=Category.objects.all().order_by('category_name'))

    class Meta:
        model = Product
        fields = ['product_name', 'product_code', 'product_images', 'product_mfg_date', 'category']
