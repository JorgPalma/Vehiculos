# Generated by Django 5.1 on 2024-08-10 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='version',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
