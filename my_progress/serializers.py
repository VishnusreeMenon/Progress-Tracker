from rest_framework import serializers
from .models import Exercise


class ExerciseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Exercise 
        # fields = ('current_weight','goal_weight','rep_count')
        fields = "__all__"