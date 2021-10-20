from django.shortcuts import render

# Create your views here.
def get_exercise_log(request):
    return render(request, 'tracker/get_exercise_log.html')
