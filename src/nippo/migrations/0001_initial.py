# Generated by Django 4.2.13 on 2024-06-27 14:29

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="NippoModel",
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
                ("title", models.CharField(max_length=100)),
                ("content", models.CharField(max_length=1000)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
