from django import forms
from .models import Tenant, UnitAssignment

class TenantForm(forms.ModelForm):
    address = forms.CharField (required=True)
    city = forms.CharField (required=True)
    pincode = forms.CharField (required=True)
    proof_type = forms.CharField (required=True)
    id_number = forms.CharField (required=True)

    class Meta:
        model = Tenant
        fields = ['user', 'address', 'city', 'pincode', 'proof_type', 'id_number']

class UnitAssignmentForm(forms.ModelForm):
    class Meta:
        model = UnitAssignment
        fields = ['agreement_end_date', 'monthly_rent_date']
