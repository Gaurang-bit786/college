# Generated by Django 4.0.6 on 2022-09-17 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('human_resource', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='slug',
            field=models.SlugField(blank=True, max_length=150, null=True),
        ),
    ]
