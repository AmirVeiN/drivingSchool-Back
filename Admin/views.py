from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Class
from .serializers import ClassSerializer, UserSerializer
from User.models import User
class AdminLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if username == 'admin' and password == 'admin':
            return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        
class CreateUser(APIView):
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
            user.delete()
            return Response({"message": "User deleted successfully"}, status=status.HTTP_202_ACCEPTED)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

class UsersView(APIView):
    def get(self, request):
        users = User.objects.exclude(user_type=3)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class GetMorabi(APIView):
    def get(self, request):
        users = User.objects.filter(user_type=1)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ClassView(APIView):
    def get(self, request):
        classes = Class.objects.all()
        serializer = ClassSerializer(classes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ClassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Class created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        class_id = request.data.get("id")
        
        if not class_id:
            return Response({"error": "Class ID not provided"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            class_instance = Class.objects.get(id=class_id)
            class_instance.delete()
            return Response({"message": "Class deleted successfully"}, status=status.HTTP_202_ACCEPTED)
        
        except Class.DoesNotExist:
            return Response({"error": "Class not found"}, status=status.HTTP_404_NOT_FOUND)
        
class ClassUserView(APIView):
    def get(self, request, class_id):
        try:
            class_instance = Class.objects.get(id=class_id)
            users = class_instance.people.all()
            users_data = [{"id": user.id, "name": user.name} for user in users]
            return Response(users_data, status=status.HTTP_200_OK)
        except Class.DoesNotExist:
            return Response({"error": "Class not found"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, class_id):
        user_id = request.data.get("userId")
        try:
            class_instance = Class.objects.get(id=class_id)
            user = User.objects.get(id=user_id)
            class_instance.people.add(user)
            return Response({"message": "User Added to class successfully"}, status=status.HTTP_201_CREATED)
        except Class.DoesNotExist:
            return Response({"error": "Class not found"}, status=status.HTTP_404_NOT_FOUND)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, class_id, user_id):
        try:
            class_instance = Class.objects.get(id=class_id)
            user = User.objects.get(id=user_id)
            class_instance.people.remove(user)
            return Response({"message": "User removed from class"}, status=status.HTTP_202_ACCEPTED)
        except Class.DoesNotExist:
            return Response({"error": "Class not found"}, status=status.HTTP_404_NOT_FOUND)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)