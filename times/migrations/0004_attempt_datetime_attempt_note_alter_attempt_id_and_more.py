# Generated by Django 4.0 on 2022-01-20 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('times', '0003_attempt_session'),
    ]

    operations = [
        migrations.AddField(
            model_name='attempt',
            name='datetime',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='attempt',
            name='note',
            field=models.CharField(max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='attempt',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='session',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]