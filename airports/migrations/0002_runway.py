# Generated by Django 4.0.1 on 2022-02-12 01:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('airports', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Runway',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('runway_number', models.IntegerField()),
                ('runway_designation', models.CharField(choices=[('L', 'Left'), ('C', 'Center'), ('R', 'Right'), ('L', 'Left')], default='N', max_length=1)),
                ('length', models.IntegerField()),
                ('width', models.IntegerField()),
                ('airport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='airports.airport')),
            ],
        ),
    ]
