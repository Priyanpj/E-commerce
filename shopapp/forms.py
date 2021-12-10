from . models import feature_products
from django import forms
# from django.forms import ModelForm
class ModeForm(forms.ModelForm):
    class Meta:
        model = feature_products
        fields = "__all__"
        # fields:['name','desc','image','price']
        # fields:['name','img','price','prod_cat','pro_desc']