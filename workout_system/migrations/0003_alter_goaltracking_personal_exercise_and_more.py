# Generated by Django 5.0.3 on 2024-03-12 17:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout_system', '0002_alter_workoutexercise_category'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='goaltracking',
            name='personal_exercise',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='workout_system.personalworkoutplan'),
        ),
        migrations.AlterField(
            model_name='goaltracking',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='goaltracking',
            name='user_weight',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='personalworkoutplan',
            name='exercise',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='workout_system.workoutexercise'),
        ),
        migrations.AlterField(
            model_name='personalworkoutplan',
            name='frequency_per_week',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='personalworkoutplan',
            name='sets',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='personalworkoutplan',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='workoutcategory',
            name='category_name',
            field=models.CharField(blank=True, max_length=35, null=True, unique=True),
        ),
    ]
