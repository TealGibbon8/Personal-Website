# Generated by Django 5.0.4 on 2024-04-11 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0002_alter_project_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="image",
            field=models.ImageField(blank=True, upload_to="media/project_images/"),
        ),
    ]
