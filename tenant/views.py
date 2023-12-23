from django.shortcuts import render, redirect
from .models import Tenant, UnitAssignment
from .forms import TenantForm, UnitAssignmentForm
from account.models import User
from property.models import Property, Unit
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def edit_tenant(request):
    user = request.user  # Assuming the user is authenticated

    # Check if the user has a related Tenant instance
    try:
        tenant = Tenant.objects.get(user=user)
    except Tenant.DoesNotExist:
        tenant = None

    if request.method == 'POST':
        form = TenantForm(request.POST, instance=tenant)
        if form.is_valid():
            updated_tenant = form.save(commit=False)
            updated_tenant.user = user  # Ensure the user remains associated with the tenant
            updated_tenant.save()
            return redirect('index')
    else:
        form = TenantForm(instance=tenant) if tenant else TenantForm()

    return render(request, 'tenant/tenant_update_form.html', {'form': form})

def view_tenant_profile(request):

    tenant_instance = Tenant.objects.get(user=request.user)
    rental_info = UnitAssignment.objects.filter(tenant=tenant_instance)
    context = [{"field_name": "Name", "field_value": tenant_instance.user.name or '-'},
               {"field_name": "Email", "field_value": tenant_instance.user.email or '-'},
               {"field_name": "Address", "field_value": tenant_instance.address or '-'},
               {"field_name": "City", "field_value": tenant_instance.city or '-'},
               {"field_name": "Pincode", "field_value": tenant_instance.pincode or '-'},
               {"field_name": "Proof type", "field_value": tenant_instance.proof_type or '-'},
               {"field_name": "Id", "field_value": tenant_instance.id_number or '-'}
               ]
    return render(request, 'tenant/view_tenant_profile.html', {"context": context, "tenant_instance": tenant_instance,
                                                               'rental_info': rental_info})


def property_list(request):
    properties = Property.objects.prefetch_related('units')
    return render(request, 'tenant/property_list.html', {'properties': properties})

@login_required(login_url='login')
def assign_unit_to_tenant(request, pk):
    unit_id = pk
    unit_instance = Unit.objects.get(unit_id=unit_id)
    tenant_instance = Tenant.objects.get(user=User.objects.get(id=request.user.id))

    if request.method == 'POST':
        form = UnitAssignmentForm(request.POST)
        if form.is_valid():
            form_instance = form.save(commit=False)
            form_instance.unit = unit_instance
            form_instance.tenant = tenant_instance
            form_instance.save()
            unit_instance.is_avail = False
            unit_instance.save()
            return redirect('index')  # Redirect upon successful assignment
    else:
        form = UnitAssignmentForm()

    return render(request, 'tenant/unit_assign_form.html', {'form': form, 'unit': unit_instance})

# not completed.
def search_view(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = Unit.objects.filter(unit_type__icontains=query)
    return render(request, 'search_results.html', {'results': results, 'query': query})