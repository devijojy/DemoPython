# Generated by Django 4.2.1 on 2023-05-28 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1994-07-25'),
            preserve_default=False,
        ),
    ]
