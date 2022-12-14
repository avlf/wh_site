# Generated by Django 4.0.6 on 2022-10-27 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wh_info', '0010_deployment_map_rule_mission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deployment_map',
            name='photo',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='strategems',
            name='type',
            field=models.CharField(choices=[('Battle Tactic Stratagem', 'Battle Tactic Stratagem'), ('Epic Deed Stratagem', 'Epic Deed Stratagem'), ('Requisition Stratagem', 'Requisition Stratagem'), ('Strategic Ploy Stratagem', 'Strategic Ploy Stratagem'), ('Wargear Stratagem', 'Wargear Stratagem')], max_length=100),
        ),
    ]
