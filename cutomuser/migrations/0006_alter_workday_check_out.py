# Generated by Django 4.2.2 on 2023-06-12 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cutomuser', '0005_rename_time_in_workday_current_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workday',
            name='check_out',
            field=models.BooleanField(default=False),
        ),
    ]