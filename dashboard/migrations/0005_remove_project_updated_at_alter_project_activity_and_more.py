# Generated by Django 5.1.6 on 2025-04-23 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_alter_project_activity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='project',
            name='activity',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='location',
            field=models.CharField(choices=[('Onsite', 'Onsite'), ('Remote', 'Remote')], default='Remote', max_length=10),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='project',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
