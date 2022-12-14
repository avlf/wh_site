# Generated by Django 4.0.6 on 2022-10-27 16:45

from django.db import migrations, models
import django_jsonform.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wh_info', '0009_alter_strategems_cost_alter_strategems_fraction_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deployment_Map',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('photo', models.CharField(max_length=100)),
                ('Deployment_Zone_A', models.IntegerField()),
                ('Deployment_Zone_b', models.IntegerField()),
                ('len_center', models.IntegerField()),
                ('disription', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('disription', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[], max_length=100)),
                ('faction_keywords', django_jsonform.models.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), blank=True, size=None)),
                ('First_rule', models.CharField(max_length=100)),
                ('Tiem_of_code', models.IntegerField()),
                ('condition_of_win', models.CharField(choices=[], max_length=100)),
                ('dop_rules', models.ManyToManyField(related_name='rule', to='wh_info.rule')),
            ],
        ),
    ]
