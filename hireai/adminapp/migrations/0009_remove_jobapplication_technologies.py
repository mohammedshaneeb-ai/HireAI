# Generated by Django 5.0.6 on 2024-05-23 05:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("adminapp", "0008_jobapplication_skills_new"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="jobapplication",
            name="technologies",
        ),
    ]
