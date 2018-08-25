from django import forms
from .models import Entry

class EntryForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    image = forms.ImageField()


'''
class EntryModelForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['title', 'description', 'image']
'''
