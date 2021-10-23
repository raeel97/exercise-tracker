from django.shortcuts import render, redirect, get_object_or_404
from .models import exercise_type
from .forms import ExerciseTypeForm


def exercise_types(request):
    types = exercise_type.objects.all()
    context = {
        'types': types
    }
    return render(request, 'tracker/exercise_types.html', context)


def add_exercise_type(request):
    if request.method == "POST":
        form = ExerciseTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exercise_types')
    form = ExerciseTypeForm()
    context = {
        'form': form
    }
    return render(request, 'tracker/add_exercise_type.html', context) 


def edit_exercise_type(request, type_id):
    type = get_object_or_404(exercise_type, id=type_id)
    if request.method == "POST":
        form = ExerciseTypeForm(request.POST, instance=type)
        if form.is_valid():
            form.save()
            return redirect('exercise_types')
    form = ExerciseTypeForm(instance=type)
    context = {
        'form': form
    }
    return render(request, 'tracker/edit_exercise_type.html', context)


def delete_exercise_type(request, type_id):
    type = get_object_or_404(exercise_type, id=type_id)
    type.delete()
    return redirect('exercise_types')
