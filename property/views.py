from django.contrib.auth.decorators import login_required
from .models import Property
from django.shortcuts import render, redirect
from .forms import PropertyForm, UnitForm

@login_required(login_url='admin_login')
def property_create(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_home')
    else:
        form = PropertyForm()
    return render(request, 'property/property_create.html', {'property_form': form})

@login_required(login_url='admin_login')
def unit_create(request, pk):
    property_instance = Property.objects.get(property_id=pk)
    if request.method == 'POST':
        form = UnitForm(request.POST)
        if form.is_valid():
            unit = form.save(commit=False)
            unit.property = property_instance
            unit.save()
            return redirect('admin_home')
    else:
        form = UnitForm()
    return render(request, 'property/unit_create.html', {'form': form, 'property_obj': property_instance})

def view_property_profile(request, pk):
    property_id = pk
    property_instance = Property.objects.prefetch_related('units').get(property_id=property_id)
    return render(request, 'property/property_profile.html', {'property_instance': property_instance})
