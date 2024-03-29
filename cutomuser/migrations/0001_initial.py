# Generated by Django 4.2.2 on 2023-06-25 19:36

import cutomuser.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('user_id', models.CharField(max_length=150, primary_key=True, serialize=False)),
                ('created', models.DateField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('gender', models.CharField(choices=[('', ''), ('M', 'M'), ('F', 'F')], max_length=2, null=True)),
                ('phone', models.CharField(max_length=10, validators=[cutomuser.validators.validate_phone])),
                ('first_name', models.CharField(max_length=200)),
                ('middle_and_last_name', models.CharField(max_length=200)),
                ('level', models.IntegerField(null=True)),
                ('role', models.CharField(choices=[('', ''), ('Staff Member', 'Staff Member'), ('Student Member', 'Student Member')], default='role', max_length=100)),
                ('course', models.CharField(max_length=300, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=255)),
                ('hourly_rate', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('archived', models.BooleanField(default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Workarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('archived', models.BooleanField(default=False, null=True)),
                ('incharge', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('job', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cutomuser.job')),
                ('members', models.ManyToManyField(blank=True, related_name='members', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-updated', '-created'],
            },
        ),
        migrations.CreateModel(
            name='Workday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_out', models.BooleanField(default=False)),
                ('check_in', models.BooleanField(default=False)),
                ('time_out', models.TimeField(auto_now_add=True)),
                ('created', models.DateTimeField(auto_now_add=True, validators=[cutomuser.validators.validate_work_day])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('workarea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cutomuser.workarea')),
            ],
            options={
                'ordering': ['-time_out', '-created'],
            },
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('is_approved', models.BooleanField(default=False)),
                ('archived', models.BooleanField(default=False, null=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cutomuser.job')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
