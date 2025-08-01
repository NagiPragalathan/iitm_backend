# Generated by Django 4.1.9 on 2025-07-22 06:36

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_contactform_grievanceform_careerform'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentAchievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='achievements/student/')),
                ('alt', models.CharField(help_text='Alt text for image', max_length=255)),
                ('unique_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('date', models.DateField()),
                ('description', ckeditor.fields.RichTextField()),
                ('relevant_link', models.URLField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_achievements', to='base.course')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_achievements', to='base.department')),
            ],
            options={
                'verbose_name': 'Student Achievement',
                'verbose_name_plural': 'Student Achievements',
                'ordering': ['-date', '-created_at'],
            },
        ),
        migrations.CreateModel(
            name='CollegeAchievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='achievements/college/')),
                ('alt', models.CharField(help_text='Alt text for image', max_length=255)),
                ('unique_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('date', models.DateField()),
                ('description', ckeditor.fields.RichTextField()),
                ('relevant_link', models.URLField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='college_achievements', to='base.course')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='college_achievements', to='base.department')),
            ],
            options={
                'verbose_name': 'College Achievement',
                'verbose_name_plural': 'College Achievements',
                'ordering': ['-date', '-created_at'],
            },
        ),
    ]
