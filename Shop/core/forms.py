from django.forms import CharField, IntegerField, ModelForm, TextInput, ModelChoiceField, FileField, Textarea, Select
from .models import Product, Category


class AddProduct(ModelForm):
    name = CharField(max_length=50, widget=TextInput(attrs={'class': "form-control", "id": "InputProductName"}))
    price = IntegerField(widget=TextInput(attrs={'class': "form-control", "id": "InputProductPrice"}))
    description = CharField(max_length=255, widget=Textarea(attrs={'class': "form-control", "id": "InputProductDescription"}))
    category = ModelChoiceField(queryset=Category.objects.all(), empty_label=None, widget=Select(attrs={'class': "form-control", "id": "InputProductCategory"}))
    image = FileField(label='Choose file')

    class Meta:
        model = Product
        fields = ['category', 'name', 'price', 'description', 'image']
