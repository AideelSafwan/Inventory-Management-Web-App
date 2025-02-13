from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.item_maintenance_form, name='item_maintenance_create'),
    path('list/', views.item_maintenance_list, name='item_maintenance_retrieve'),
    path('<int:id>/', views.item_maintenance_form, name='item_maintenance_update'),
    path('delete/<int:id>/', views.item_maintenance_delete, name='item_maintenance_delete')
]