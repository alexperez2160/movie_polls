# Generated by Django 2.1.4 on 2018-12-24 14:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_auto_20181224_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]