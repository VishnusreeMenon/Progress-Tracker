from urllib import request

from django import forms

class FilterForm(forms.Form):
    
    filter_by = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    
    
    