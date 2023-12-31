# Generated by Django 5.0 on 2023-12-23 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenant', '0002_remove_tenant_name_tenant_city'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tenant',
            old_name='document_proof',
            new_name='proof_type',
        ),
        migrations.RemoveField(
            model_name='tenant',
            name='aadhar_number',
        ),
        migrations.RemoveField(
            model_name='tenant',
            name='is_verified',
        ),
        migrations.RemoveField(
            model_name='tenant',
            name='tenant_image',
        ),
        migrations.RemoveField(
            model_name='tenant',
            name='voter_id',
        ),
        migrations.AddField(
            model_name='tenant',
            name='id_number',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
