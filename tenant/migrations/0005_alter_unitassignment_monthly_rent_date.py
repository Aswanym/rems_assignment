# Generated by Django 5.0 on 2023-12-23 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenant', '0004_unitassignment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unitassignment',
            name='monthly_rent_date',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]