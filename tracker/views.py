from django.shortcuts import render, redirect
from .models import exercise_type
# Create your views here.
def exercise_types(request):
    types = exercise_type.objects.all()
    context = {
        'types': types
    }
    return render(request, 'tracker/exercise_types.html', context)


def add_exercise_type(request):
    if request.method == "POST":
        name = request.POST.get('id_name')
        measurement = request.POST.get('id_measurement')
        exercise_type.objects.create(name=name, measurement=measurement)
        return redirect('get_exercise_types')
    return render(request, 'tracker/add_exercise_type.html')
