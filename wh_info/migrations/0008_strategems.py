# Generated by Django 4.0.6 on 2022-10-18 16:16

from django.db import migrations, models
import django_jsonform.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wh_info', '0007_remove_minroster_commanders_remove_minroster_elites_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Strategems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cost', models.IntegerField(blank=True, max_length=100)),
                ('type', django_jsonform.models.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), blank=True, size=None)),
                ('fraction', django_jsonform.models.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), blank=True, size=None)),
                ('disription_first', models.CharField(blank=True, max_length=100)),
                ('disription_second', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
