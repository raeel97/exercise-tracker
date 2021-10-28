"""exercise_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tracker import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.exercise_types, name="exercise_types"),
    path('add_exercise_type', views.add_exercise_type, name="add_exercise_type"),
    path('edit_exercise_type/<type_id>', views.edit_exercise_type, name="edit_exercise_type"),
    path('delete_exercise_type/<type_id>', views.delete_exercise_type, name="delete_exercise_type"),
    path('exercise_sessions', views.exercise_sessions, name="exercise_sessions"),
    path('add_exercise_session', views.add_exercise_session, name="add_exercise_session"),
    path('edit_exercise_session/<session_id>', views.edit_exercise_session, name="edit_exercise_session"),
    path('delete_exercise_session/<session_id>', views.delete_exercise_session, name="delete_exercise_session"),
]