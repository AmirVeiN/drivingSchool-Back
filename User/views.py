from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from Admin.serializers import ClassSerializer, UserSerializer
from .models import User

class UserLoginView(APIView):
    
    def post(self, request):
        codemeli = request.data.get('codemeli')
        
        if codemeli:
            user_exists = User.objects.get(codemeli=codemeli)
            
            if user_exists:
                return Response({"message": "Login successful", "name" : user_exists.name , "telephone" : user_exists.telephone}, status=status.HTTP_200_OK)
            
            else :
                return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


class GetUserView(APIView):
    
    def post(self, request):
        
        codemeli = request.data.get('codemeli')
        
        try:
            user = User.objects.get(codemeli=codemeli)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except User.DoesNotExist:
            return Response({"error": "کاربر یافت نشد"}, status=status.HTTP_404_NOT_FOUND)
        
class UserClassesView(APIView):
    
    def post(self, request):
        
        codemeli = request.data.get("codemeli")
        
        if not codemeli:
            return Response({"error": "کد ملی ارسال نشده است."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(codemeli=codemeli)
            user_classes = user.classes.all() 
            serializer = ClassSerializer(user_classes, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except User.DoesNotExist:
            return Response({"error": "کاربر یافت نشد."}, status=status.HTTP_404_NOT_FOUND)