from django.shortcuts import render, redirect
from .models import ItemMaintenance
from .forms import ItemMaintenanceForm

# Create your views here.
def item_maintenance_list(request):
    context = {'item_maintenance_list':ItemMaintenance.objects.all()}
    return render(request, "item_maintenance/item_maintenance_list.html", context)

def item_maintenance_form(request, id = 0):
    if request.method == "GET":
        if id == 0:
            form = ItemMaintenanceForm()
        else:
            item = ItemMaintenance.objects.get(pk = id)
            form = ItemMaintenanceForm(instance = item)
        return render(request, "item_maintenance/item_maintenance_form.html",{'form':form})
    else:
        if id == 0:
            form = ItemMaintenanceForm(request.POST)
        else:
            item = ItemMaintenance.objects.get(pk = id)
            form = ItemMaintenanceForm(request.POST, instance = item)
        if form.is_valid():
            form.save()
        return redirect('/item_maintenance/list')

def item_maintenance_delete(request, id):
    item_maintenance = ItemMaintenance.objects.get(pk = id)
    item_maintenance.delete()
    return redirect('/item_maintenance/list')