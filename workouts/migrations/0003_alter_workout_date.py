# Generated by Django 4.0.3 on 2022-03-23 01:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0002_alter_set_seconds_resting_alter_set_seconds_working'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
