from django.shortcuts import render
from django.http import JsonResponse
from .models import Pet
from rest_framework.views import APIView
from apps.pets.serializers import PetSerializer

# Create Pet
class CreatePet(APIView):
    def post(self, request, *args, **kwargs):
        serializer = PetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    def put(self, request, *args, **kwargs):
        pet = Pet.objects.get(id=kwargs['id'])
        serializer = PetSerializer(pet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    def delete(self, request, *args, **kwargs):
        pet = Pet.objects.get(id=kwargs['id'])
        pet.delete()
        return JsonResponse({"success": 'Deleted'}, status=200)

# Upload pet image
class UploadPetImage(APIView):
    def post(self, request, *args, **kwargs):
        pet = Pet.objects.get(id=kwargs['id'])
        pet.photoUrls = request.data.get('photoUrls')
        pet.save()
        return JsonResponse({"success": 'Uploaded'}, status=200)

# Get pet by status or id or tags using query params
class GetPetbyStatus(APIView):
    def get(self, request, *args, **kwargs):
        if request.GET.get('status'):
            pets = Pet.objects.filter(status=request.GET.get('status'))
        elif request.GET.get('id'):
            pets = Pet.objects.filter(id=request.GET.get('id'))
        elif request.GET.get('tags'):
            pets = Pet.objects.filter(tags__name=request.GET.get('tags'))
        else:
            pets = Pet.objects.all()
        serializer = PetSerializer(pets, many=True)
        return JsonResponse(serializer.data, status=200, safe=False)


class GetPetbyQuery(APIView):
    def get(self, request, *args, **kwargs):
        if request.GET.get('status'):
            pets = Pet.objects.filter(status=request.GET.get('status'))
        elif request.GET.get('id'):
            pets = Pet.objects.filter(id=request.GET.get('id'))
        elif request.GET.get('tags'):
            pets = Pet.objects.filter(tags__name=request.GET.get('tags'))
        else:
            pets = Pet.objects.all()
        serializer = PetSerializer(pets, many=True)
        return JsonResponse(serializer.data, status=200, safe=False)

