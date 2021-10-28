from django.shortcuts import render, redirect, get_object_or_404
from .models import exercise_type, exercise_session
from .forms import ExerciseTypeForm, ExerciseSessionForm

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


def exercise_sessions(request):
    sessions = exercise_session.objects.all()
    context = {
        'sessions': sessions
    }
    return render(request, 'tracker/exercise_sessions.html', context)

def add_exercise_session(request):
    if request.method == "POST":
        form = ExerciseSessionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exercise_sessions')
    form = ExerciseSessionForm()
    context = {
        'form': form
    }
    return render(request, 'tracker/add_exercise_sessions.html', context)
    
def edit_exercise_session(request, session_id):
    session = get_object_or_404(exercise_session, id=session_id)
    if request.method == "POST":
        form = ExerciseSessionForm(request.POST, instance=session)
        if form.is_valid():
            form.save()
            return redirect('exercise_sessions')
    form = ExerciseSessionForm(instance=session)
    context = {
        'form': form
    }
    return render(request, 'tracker/edit_exercise_session.html', context) 

def delete_exercise_session(request, session_id):
    session = get_object_or_404(exercise_session, id=session_id)
    session.delete()
    return redirect('exercise_sessions')