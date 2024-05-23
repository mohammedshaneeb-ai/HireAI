# Generated by Django 5.0.6 on 2024-05-21 06:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("adminapp", "0006_alter_jobapplication_score"),
    ]

    operations = [
        migrations.AddField(
            model_name="jobapplication",
            name="score_summary",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="jobapplication",
            name="score",
            field=models.DecimalField(
                decimal_places=2,
                max_digits=5,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(100),
                ],
            ),
        ),
    ]
