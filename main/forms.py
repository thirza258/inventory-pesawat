from django.forms import ModelForm
from .models import Item
from django import forms
from django.contrib.auth.models import User

class ItemForm(ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all(), required=True)

    class Meta:
        model = Item
        fields = ['user', 'name', 'amount', 'description', 'engine', 'winglet']
