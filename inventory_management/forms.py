from django import forms
from .models import InventoryManagement

class InventoryManagementForm(forms.ModelForm):
    class Meta:
        model = InventoryManagement
        fields = ('code', 'price', 'category', 'description')

    def __init__(self, *args, **kwargs):
        super(InventoryManagementForm, self).__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Select Category'
        self.fields['description'].required = False