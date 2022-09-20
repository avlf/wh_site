# Generated by Django 4.0.6 on 2022-09-13 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wh_info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('range', models.CharField(blank=True, max_length=100)),
                ('type', models.CharField(blank=True, max_length=100)),
                ('strength', models.CharField(blank=True, max_length=100)),
                ('armor_penetration', models.CharField(blank=True, max_length=100)),
                ('damage', models.CharField(blank=True, max_length=100)),
                ('abilities', models.TextField(blank=True, max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='character',
            name='abilities',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='character',
            name='battlefield_role',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='character',
            name='faction_keywords',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='character',
            name='keywors',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='character',
            name='power_rating',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='character',
            name='profile',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='character',
            name='unit_composition',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='character',
            name='wargear',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='character',
            name='weapons',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='character',
            name='description',
            field=models.TextField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='character',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]