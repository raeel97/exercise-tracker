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
        fields = ['date', 'type', 'measurement', 'additonal_notes']
        # type_choices = exercise_type.objects.all()
        # exercise_type_measurements = {}
        # for choice in type_choices:
        #     exercise_type_measurements.update({choice.name: choice.measurement})
        # if tracker.forms.ExerciseSessionForm.Meta.fields[1] == exercise_type_measurements.keys():
        #     placeholder = value
        widgets = {
            'date': DateInput(),
            'measurement': forms.TextInput(attrs={'placeholder': 'must match type measurement'}),
        }