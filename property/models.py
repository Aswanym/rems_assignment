from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Property(models.Model):
    property_id = models.BigAutoField(primary_key=True)
    property_name = models.CharField(null=True, blank=True, max_length=255)
    address = models.CharField(null=True, blank=True, max_length=255)
    city = models.CharField(null=True, blank=True, max_length=255)
    pincode = models.CharField(null=True, blank=True, max_length=255)

class Unit(models.Model):

    class UnitType(models.TextChoices):
        ONE_BHK = '1BHK', _('1BHK')
        TWO_BHK = '2BHK', _ ('2BHK')
        THREE_BHK = '3BHK', _ ('3BHK')
        FOUR_BHK = '4BHK', _ ('4BHK')

    unit_id = models.BigAutoField(primary_key=True)
    unit_name = models.CharField(max_length=255, null=True, blank=True)
    property = models.ForeignKey(Property, related_name='units', on_delete=models.CASCADE)
    rent_cost = models.PositiveIntegerField(default=0)
    unit_type = models.CharField(null=True, blank=True, max_length=10, choices=UnitType.choices)
    is_avail = models.BooleanField(default=True)
