# Generated by Django 3.0.4 on 2020-03-05 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='id',
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='vid',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
