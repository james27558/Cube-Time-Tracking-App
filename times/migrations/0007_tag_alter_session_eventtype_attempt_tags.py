# Generated by Django 4.0 on 2022-02-01 09:55

from django.db import migrations, models
import django.db.models.deletion
import times.models


class Migration(migrations.Migration):

    dependencies = [
        ('times', '0006_cube_eventtype_session_note_session_cubeused_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('name', models.CharField(max_length=200, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AlterField(
            model_name='session',
            name='eventType',
            field=models.ForeignKey(default=times.models.eventType_default, on_delete=django.db.models.deletion.RESTRICT, to='times.eventtype'),
        ),
        migrations.AddField(
            model_name='attempt',
            name='tags',
            field=models.ManyToManyField(to='times.Tag'),
        ),
    ]