from django import forms
from .models import List

class ListFrom(forms.ModelForm):
    class Meta:
        model = List
        fields = ["item","completed"]
