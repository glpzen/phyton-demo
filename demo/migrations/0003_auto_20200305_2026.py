# Generated by Django 3.0.4 on 2020-03-05 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_auto_20200305_2025'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehicle',
            old_name='vid',
            new_name='id',
        ),
    ]
