# Generated by Django 5.0.6 on 2024-05-18 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("adminapp", "0003_jobposting_company_profile"),
    ]

    operations = [
        migrations.AddField(
            model_name="jobposting",
            name="requirements",
            field=models.TextField(blank=True),
        ),
    ]
