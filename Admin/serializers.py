from rest_framework import serializers
from User.models import User
from .models import Class

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'address', 'codemeli', 'sen','telephone', 'noe_tadris', 'user_type']

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['id', 'address', 'class_number', 'class_time', 'class_created', 'morabi']