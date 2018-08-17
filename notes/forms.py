from django import forms
from .models import Entry


class EntryModelForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['title', 'description', 'image']
