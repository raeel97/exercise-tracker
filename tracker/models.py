from datetime import date
from django.db import models
from django.utils.translation import gettext as _


# Create your models here.


class exercise_type(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)
    measurement = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return self.name
   

class exercise_session(models.Model):
    type_select = models.ForeignKey(exercise_type, on_delete=models.CASCADE)
    measurement = models.CharField(max_length=20, null=False, blank=False)
    session_date = models.DateField(_("Date"), default=date.today)
    additonal_notes = models.CharField(max_length=100, null=False, blank=True)