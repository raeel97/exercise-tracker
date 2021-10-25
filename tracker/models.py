from django.db import models

# Create your models here.


class exercise_type(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)
    measurement = models.CharField(max_length=20, null=False, blank=False)
    # sessions = models.ForeignKey(
    #     'Exercise Sessions',
    #     on_delete=models.CASCADE,
    # )
    def __str__(self):
        return self.name


type_choices = exercise_type.objects.all()
EXERCISE_TYPE_NAMES_LIST = []
for choice in type_choices:
    EXERCISE_TYPE_NAMES_LIST.append((choice.name, choice.name.upper()))
EXERCISE_TYPE_NAMES = tuple(EXERCISE_TYPE_NAMES_LIST)
   

class exercise_session(models.Model):
    date = models.DateField()
    type = models.CharField(max_length=20, null=False, choices=EXERCISE_TYPE_NAMES, blank=False, default='select exercise type')
    measurement = models.CharField(max_length=20, null=False, blank=False)
    additonal_notes = models.CharField(max_length=100, null=True, blank=True)

    
