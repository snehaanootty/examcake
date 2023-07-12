from myapp.models import Cake
from django import forms


class CakeForm(forms.ModelForm):
    class Meta:
        model=Cake
        fields="__all__"
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "price":forms.TextInput(attrs={"class":"form-control"}),
            "layer":forms.TextInput(attrs={"class":"form-control"}),
            "shape":forms.Select(attrs={"class":"form-control"})
        }