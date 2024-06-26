from django import forms


class ProductForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    price = forms.IntegerField()
    quantity = forms.IntegerField()
    image = forms.ImageField()