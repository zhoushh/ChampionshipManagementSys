# Generated by Django 2.0.3 on 2018-06-06 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('championship', '0009_timetableforleague'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='championship',
            name='timetable',
        ),
    ]