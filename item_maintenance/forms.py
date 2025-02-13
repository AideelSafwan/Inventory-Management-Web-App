from django import forms
from .models import ItemMaintenance

class ItemMaintenanceForm(forms.ModelForm):
    class Meta:
        model = ItemMaintenance
        fields = ('code', 'price', 'category', 'description')

    def __init__(self, *args, **kwargs):
        super(ItemMaintenanceForm, self).__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Select Category'
        self.fields['description'].required = False