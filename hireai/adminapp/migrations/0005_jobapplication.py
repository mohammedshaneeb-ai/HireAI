# Generated by Django 5.0.6 on 2024-05-21 05:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("adminapp", "0004_jobposting_requirements"),
    ]

    operations = [
        migrations.CreateModel(
            name="JobApplication",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("job_id", models.CharField(max_length=50)),
                ("job_title", models.CharField(max_length=100)),
                ("candidate_name", models.CharField(max_length=100)),
                (
                    "score",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=5,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(100),
                        ],
                    ),
                ),
                ("phone", models.CharField(max_length=15)),
                (
                    "email",
                    models.EmailField(
                        max_length=254,
                        validators=[django.core.validators.EmailValidator],
                    ),
                ),
                (
                    "experience",
                    models.PositiveIntegerField(help_text="Experience in years"),
                ),
                (
                    "age",
                    models.PositiveIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(10),
                            django.core.validators.MaxValueValidator(100),
                        ]
                    ),
                ),
                (
                    "resume_link",
                    models.URLField(validators=[django.core.validators.URLValidator]),
                ),
                ("skills", models.JSONField(help_text="List of skills")),
                ("technologies", models.JSONField(help_text="List of technologies")),
            ],
        ),
    ]
