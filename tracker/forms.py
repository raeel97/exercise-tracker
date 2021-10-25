from django import forms
from .models import exercise_type, exercise_session


class ExerciseTypeForm(forms.ModelForm):
    class Meta:
        model = exercise_type
        fields = ['name', 'measurement']

class ExerciseSessionForm(forms.ModelForm):
    class Meta:
        model = exercise_session
        fields = [
            'date', 
            'type', 
            'measurement', 
            'additonal_notes'
            ]