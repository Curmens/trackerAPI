from django.urls import path
from .views import CreatePet, UploadPetImage, GetPetbyQuery


urlpatterns = [
    path('', CreatePet.as_view(), name='Pet'),
    path('find/', GetPetbyQuery.as_view(), name='Get Pet'),
    path('<int:id>/uploadImage/', UploadPetImage.as_view(), name='Upload Pet Image'),
]