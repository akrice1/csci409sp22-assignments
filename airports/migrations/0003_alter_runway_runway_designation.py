# Generated by Django 4.0.1 on 2022-02-17 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airports', '0002_runway'),
    ]

    operations = [
        migrations.AlterField(
            model_name='runway',
            name='runway_designation',
            field=models.CharField(choices=[('L', 'Left'), ('C', 'Center'), ('R', 'Right'), ('N', 'None')], default='N', max_length=1),
        ),
    ]
