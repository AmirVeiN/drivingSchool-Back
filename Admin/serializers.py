from rest_framework import serializers
from User.models import User
from .models import Class

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','name', 'address', 'codemeli', 'sen','telephone', 'user_type']

class ClassSerializer(serializers.ModelSerializer):
    morabi_name = serializers.CharField(source='morabi.name', read_only=True)

    class Meta:
        model = Class
        fields = ['id', 'address', 'class_number', 'class_time', 'class_created','morabi', 'morabi_name', 'noe_tadris']
        extra_kwargs = {
            'morabi': {'write_only': True},
            'people' : {'write_only': True}
        }