# Generated by Django 5.0 on 2023-12-23 08:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0002_alter_unit_property_alter_unit_unit_type'),
        ('tenant', '0003_rename_document_proof_tenant_proof_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnitAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agreement_end_date', models.DateField(blank=True, null=True)),
                ('monthly_rent_date', models.DateField(blank=True, null=True)),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rental_info', to='tenant.tenant')),
                ('unit', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='property.unit')),
            ],
        ),
    ]
