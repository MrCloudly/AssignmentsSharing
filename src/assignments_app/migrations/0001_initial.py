# Generated by Django 4.2.6 on 2023-10-10 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField()),
                ('time_cost', models.FloatField()),
                ('priority', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('pseudonym', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_type', models.CharField(choices=[('NEW', 'New'), ('IN_PROGRESS', 'In Progress'), ('DONE', 'Done')], default='NEW', max_length=12)),
                ('occurrence_time', models.DateTimeField(auto_now_add=True)),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='statuses', to='assignments_app.assignment')),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignments_app.assignment')),
                ('developer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignments_app.developer')),
            ],
        ),
        migrations.AddField(
            model_name='developer',
            name='assignments',
            field=models.ManyToManyField(through='assignments_app.Issue', to='assignments_app.assignment'),
        ),
    ]
