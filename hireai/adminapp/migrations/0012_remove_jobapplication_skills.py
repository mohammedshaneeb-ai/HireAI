# Generated by Django 5.0.6 on 2024-05-23 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("adminapp", "0011_alter_jobapplication_options"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="jobapplication",
            name="skills",
        ),
    ]