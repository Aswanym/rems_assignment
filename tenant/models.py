from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from account.models import User
from property.models import Unit
# Create your models here.

class Tenant(models.Model):
    class DocumentProofType(models.TextChoices):
        AADHAR = 'AADHAR', _('Aadhar card')
        VOTER = 'VOTER', _('Voter id')

    tenant_id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(null=True, blank=True, max_length=255)
    city = models.CharField(null=True, blank=True, max_length=255)
    pincode = models.CharField(null=True, blank=True, max_length=255)
    proof_type = models.CharField(null=True, blank=True, max_length=10, choices=DocumentProofType.choices)
    id_number = models.CharField(null=True, blank=True, max_length=255)


@receiver(post_save, sender=User)
def create_tenant_profile(sender, instance, created, **kwargs):
    if created:
        Tenant.objects.create(user=instance)

class UnitAssignment(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='rental_info')
    unit = models.OneToOneField(Unit, on_delete=models.CASCADE)
    agreement_end_date = models.DateField(null=True, blank=True)
    monthly_rent_date = models.CharField(max_length=255, blank=True, null=True)
