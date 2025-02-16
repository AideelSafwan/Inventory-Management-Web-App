from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.inventory_management_form, name='inventory_management_create'),
    path('list/', views.inventory_management_list, name='inventory_management_retrieve'),
    path('<int:id>/', views.inventory_management_form, name='inventory_management_update'),
    path('delete/<int:id>/', views.inventory_management_delete, name='inventory_management_delete')
]