from django import forms
from .models import exercise_type


class ExerciseTypeForm(forms.ModelForm):
    class Meta:
        model = exercise_type
        fields = ['name', 'measurement']