# Generated by Django 4.0.6 on 2022-10-27 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wh_info', '0012_keywords'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='keywors',
        ),
        migrations.AddField(
            model_name='character',
            name='keywords',
            field=models.ManyToManyField(related_name='keywords', to='wh_info.keywords'),
        ),
    ]
