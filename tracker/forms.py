from django import forms
from .models import exercise_type, exercise_session


class ExerciseTypeForm(forms.ModelForm):
    class Meta:
        model = exercise_type
        fields = ['name', 'measurement']


class DateInput(forms.DateInput):
    input_type = 'date'


class ExerciseSessionForm(forms.ModelForm):

    class Meta:
        model = exercise_session
        fields = ['type_select', 'measurement', 'session_date', 'additonal_notes']
        widgets = {
            'session_date': DateInput(),
        }