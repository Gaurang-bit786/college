# Generated by Django 4.0.6 on 2022-10-11 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0002_notice_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='notice/'),
        ),
    ]
