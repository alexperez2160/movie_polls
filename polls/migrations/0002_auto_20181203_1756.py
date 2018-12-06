# Generated by Django 2.1.3 on 2018-12-03 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='question',
            new_name='movie',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='movie',
            new_name='movie_text',
        ),
        migrations.AlterField(
            model_name='movie',
            name='rel_date',
            field=models.DateTimeField(verbose_name='Release Date'),
        ),
    ]