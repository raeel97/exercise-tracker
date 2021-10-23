from django.contrib import admin
from .models import exercise_type, exercise_session
# Register your models here.

admin.site.register(exercise_type)
admin.site.register(exercise_session)