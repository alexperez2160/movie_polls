# Generated by Django 2.1.4 on 2018-12-21 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_auto_20181204_0844'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='rel_date',
        ),
    ]
