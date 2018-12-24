# Generated by Django 2.1.4 on 2018-12-24 14:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_remove_movie_rel_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published'),
            preserve_default=False,
        ),
    ]