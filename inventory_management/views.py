from django.shortcuts import render, redirect
from .models import InventoryManagement
from .forms import InventoryManagementForm

# Create your views here.
def inventory_management_list(request):
    context = {'inventory_management_list':InventoryManagement.objects.all()}
    return render(request, "inventory_management/inventory_management_list.html", context)

def inventory_management_form(request, id = 0):
    if request.method == "GET":
        if id == 0:
            form = InventoryManagementForm()
        else:
            item = InventoryManagement.objects.get(pk = id)
            form = InventoryManagementForm(instance = item)
        return render(request, "inventory_management/inventory_management_form.html",{'form':form})
    else:
        if id == 0:
            form = InventoryManagementForm(request.POST)
        else:
            item = InventoryManagement.objects.get(pk = id)
            form = InventoryManagementForm(request.POST, instance = item)
        if form.is_valid():
            form.save()
        return redirect('/inventory_management/list')

def inventory_management_delete(request, id):
    inventory_management = InventoryManagement.objects.get(pk = id)
    inventory_management.delete()
    return redirect('/inventory_management/list')