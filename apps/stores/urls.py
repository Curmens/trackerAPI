from django.urls import path, include
from .views import Inventory, FindStoreById

urlpatterns = [
    path('', Inventory.as_view(), name='Inventory'),
    path('<int:id>/', FindStoreById.as_view(), name='Find Store By Id'),
]
