# Generated by Django 5.0.6 on 2024-05-23 05:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("adminapp", "0012_remove_jobapplication_skills"),
    ]

    operations = [
        migrations.RenameField(
            model_name="jobapplication",
            old_name="skills_new",
            new_name="skills",
        ),
    ]
