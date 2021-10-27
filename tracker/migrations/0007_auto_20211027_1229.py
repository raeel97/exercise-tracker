# Generated by Django 3.2.8 on 2021-10-27 12:29

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0006_exercise_session_two'),
    ]

    operations = [
        migrations.DeleteModel(
            name='exercise_session_two',
        ),
        migrations.RemoveField(
            model_name='exercise_session',
            name='type',
        ),
        migrations.AddField(
            model_name='exercise_session',
            name='additonal_notes',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='exercise_session',
            name='measurement',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exercise_session',
            name='session_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='exercise_session',
            name='type_select',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='tracker.exercise_type'),
            preserve_default=False,
        ),
    ]
