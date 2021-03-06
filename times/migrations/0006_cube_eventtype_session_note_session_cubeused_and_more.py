# Generated by Django 4.0 on 2022-01-29 13:03

from django.db import migrations, models
import django.db.models.deletion
import times.models


class Migration(migrations.Migration):

    dependencies = [
        ('times', '0005_remove_session_date_session_enddatetime_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cube',
            fields=[
                ('name', models.CharField(max_length=200, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('name', models.CharField(max_length=200, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='session',
            name='note',
            field=models.CharField(max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='session',
            name='cubeUsed',
            field=models.ForeignKey(default=times.models.cube_default, on_delete=django.db.models.deletion.RESTRICT, to='times.cube'),
        ),
        migrations.AddField(
            model_name='session',
            name='eventType',
            field=models.ForeignKey(default=times.models.eventType_default, null=True, on_delete=django.db.models.deletion.SET_NULL, to='times.eventtype'),
        ),
    ]
