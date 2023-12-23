from django import forms
from .models import Property, Unit

class PropertyForm(forms.ModelForm):
    property_name = forms.CharField(required=True)
    address = forms.CharField(required=True)
    city = forms.CharField(required=True)
    pincode = forms.CharField(required=True)

    class Meta:
        model = Property
        fields = ['property_name', 'address', 'city', 'pincode']

class UnitForm(forms.ModelForm):
    rent_cost = forms.CharField(required=True)
    unit_type = forms.CharField(required=True)
    unit_name = forms.CharField (required=True)

    class Meta:
        model = Unit
        fields = ['unit_name', 'rent_cost', 'unit_type']

    def __init__(self, *args, **kwargs):
        super(UnitForm, self).__init__(*args, **kwargs)
        self.fields['unit_type'].widget = forms.Select(choices=Unit.UnitType.choices)