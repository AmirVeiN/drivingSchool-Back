from rest_framework import serializers
from User.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'address', 'codemeli', 'telephon', 'noe_tadris', 'user_type']

