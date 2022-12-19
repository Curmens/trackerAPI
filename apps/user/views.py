from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User
from rest_framework.views import APIView
from apps.user.serializers import UserSerializer, ChangePasswordSerializer

# create user
class CreateUser(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


class UserInfo(APIView):
    def get(self, request, *args, **kwargs):
        try:
            user = User.objects.get(username=kwargs['username'])
            serializer = UserSerializer(user)
            return JsonResponse(serializer.data, status=200)
        except Exception as e:
            print(e)
            return JsonResponse({"message": 'User not found'}, status=400)

    def put(self, request, *args, **kwargs):
        user = User.objects.get(username=kwargs['username'])
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    def delete(self, request, *args, **kwargs):
        user = User.objects.get(username=kwargs['username'])
        user.delete()
        return JsonResponse({"success": 'Deleted'}, status=200)


# create user with list
class CreateUserWithList(APIView):
    def post(self, request):
        responses = []
        for user in request.data:
            serializer = UserSerializer(data=user)
            if serializer.is_valid():
                serializer.save()
                responses.append(serializer.data)
            else:
                return JsonResponse(serializer.errors, status=400)
        return JsonResponse(responses, status=201, safe=False)

# login
class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        # return success if pair is correct
        if username and password:
            try:
                user = User.objects.get(username=username)
            except Exception as e:
                print(e)
                return JsonResponse({"success": False}, status=400)
            
            # unhash password
            if user.check_password(password):
                return JsonResponse({"success": 'Logged In'}, status=200)
            else:
                return JsonResponse({"success": 'Details Incorrect'}, status=400)
        else:
            return JsonResponse({"success": False}, status=400)

# logout
class LogoutView(APIView):
    def post(self, request):
        return JsonResponse({"success": 'Logged Out'}, status=200)



    
