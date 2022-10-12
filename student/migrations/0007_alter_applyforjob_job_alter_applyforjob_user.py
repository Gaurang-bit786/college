# Generated by Django 4.0.6 on 2022-10-07 18:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('human_resource', '0004_alter_job_options'),
        ('student', '0006_alter_applyforjob_job_alter_applyforjob_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applyforjob',
            name='job',
            field=models.ManyToManyField(related_name='jobs', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='applyforjob',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_query_name='user_jobs', to='human_resource.job'),
        ),
    ]
