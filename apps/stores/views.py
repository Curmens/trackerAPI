from django.shortcuts import render
from django.http import JsonResponse
from .models import Store
from rest_framework.views import APIView
from apps.stores.serializers import StoreSerializer


class Inventory(APIView):
    # return count of orders by status - approved, delivered, pending
    def get(self, request, *args, **kwargs):
        inventory = Store.objects.all()
        serializer = StoreSerializer(inventory, many=True)

        approved = 0
        delivered = 0
        pending = 0

        for i in serializer.data:
            if i['status'] == 'approved':
                approved += 1
            elif i['status'] == 'delivered':
                delivered += 1
            else:
                pending += 1

        return JsonResponse({'approved': approved, 'delivered': delivered, 'pending': pending}, status=200)

# find store by id
class FindStoreById(APIView):
    def get(self, request, *args, **kwargs):
        store = Store.objects.get(id=kwargs['id'])
        serializer = StoreSerializer(store)
        return JsonResponse(serializer.data, status=200)
    
    def delete(self, request, *args, **kwargs):
        store = Store.objects.get(id=kwargs['id'])
        store.delete()
        return JsonResponse({"success": 'Deleted'}, status=200)