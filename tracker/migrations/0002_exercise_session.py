# Generated by Django 3.2.8 on 2021-10-23 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='exercise_session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('type', models.CharField(max_length=20)),
                ('measurement', models.CharField(max_length=20)),
                ('additonal_notes', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
