# Generated by Django 4.0.1 on 2022-02-16 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat', models.CharField(max_length=10)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ticket_class', models.CharField(choices=[('F', 'First Class'), ('B', 'Business Class'), ('M', 'Main Class')], default=None, max_length=1)),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tickets.reservation')),
            ],
        ),
    ]
