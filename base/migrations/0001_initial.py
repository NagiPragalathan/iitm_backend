# Generated by Django 4.2.7 on 2025-07-15 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('ug', models.BooleanField(default=False)),
                ('pg', models.BooleanField(default=False)),
                ('phd', models.BooleanField(default=False)),
                ('about', models.TextField()),
                ('vision', models.TextField()),
                ('mission', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='DepartmentContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='department/contacts/')),
                ('alt', models.CharField(max_length=255)),
                ('heading', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='QuickLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('link', models.URLField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quick_links', to='base.department')),
            ],
        ),
        migrations.CreateModel(
            name='ProgramOffered',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='department/programs/')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('explore_link', models.URLField()),
                ('apply_link', models.URLField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='programs', to='base.department')),
            ],
        ),
        migrations.CreateModel(
            name='POPSO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='po_pso_peo', to='base.department')),
            ],
        ),
        migrations.CreateModel(
            name='NumberData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=50)),
                ('symbol', models.CharField(blank=True, choices=[('+', '+'), ('%', '%'), (None, 'None')], max_length=1, null=True)),
                ('text', models.CharField(max_length=255)),
                ('featured', models.BooleanField(default=False)),
                ('unique_id', models.CharField(max_length=50, unique=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='numbers', to='base.department')),
            ],
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='department/facilities/')),
                ('heading', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('alt', models.CharField(max_length=255)),
                ('link_blank', models.BooleanField(default=False)),
                ('blank_content', models.TextField(blank=True, null=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='facilities', to='base.department')),
            ],
        ),
        migrations.CreateModel(
            name='DepartmentAbout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='department/about/')),
                ('alt', models.CharField(max_length=255)),
                ('unique_id', models.CharField(max_length=50, unique=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='about_sections', to='base.department')),
            ],
        ),
        migrations.AddField(
            model_name='department',
            name='contact',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.departmentcontact'),
        ),
        migrations.CreateModel(
            name='Curriculum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('file', models.FileField(upload_to='department/curriculum/')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='curriculum', to='base.department')),
            ],
        ),
        migrations.CreateModel(
            name='CTA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=255)),
                ('link', models.URLField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ctas', to='base.department')),
            ],
        ),
        migrations.CreateModel(
            name='Benefit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(upload_to='department/benefits/')),
                ('text', models.CharField(max_length=255)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='benefits', to='base.department')),
            ],
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='department/banners/')),
                ('alt', models.CharField(max_length=255)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='banners', to='base.department')),
            ],
        ),
    ]
