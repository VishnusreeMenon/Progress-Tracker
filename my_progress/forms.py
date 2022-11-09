from urllib import request
from .models import Exercise
from django import forms
from django.contrib.auth.decorators import login_required


class AddExerciseForm(forms.ModelForm):
    exercise_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    rep_count = forms.IntegerField(widget=forms.NumberInput(attrs= {'class' : 'form-control'}))
    goal_weight = forms.IntegerField(widget=forms.NumberInput(attrs= {'class' : 'form-control'}))
    current_weight = forms.IntegerField(widget=forms.NumberInput(attrs= {'class' : 'form-control'}))

    
    class Meta:
        model = Exercise
        fields=('exercise_name','current_weight','goal_weight','rep_count')