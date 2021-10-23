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

class exercise_session(models.Model):
    date = models.DateField()
    type = models.CharField(max_length=20, null=False, blank=False)
    measurement = models.CharField(max_length=20, null=False, blank=False)
    additonal_notes = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
