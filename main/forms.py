from django.forms import ModelForm
from .models import Item
from django import forms
from django.contrib.auth.models import User

class ItemForm(ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all(), required=False)

    class Meta:
        model = Item
        fields = ['name', 'amount', 'description', 'engine', 'winglet', 'image']
        widget = {
            'name': forms.TextInput(attrs={'class': 'form-control','style': 'border-color: blue;',}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'engine': forms.Select(attrs={'class': 'form-control'}),
            'winglet': forms.CheckboxInput( attrs={'class': 'form-control'}),
            'image': forms.URLInput(attrs={'class': 'form-control'}),
        }
