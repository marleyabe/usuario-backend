from rest_framework import serializers
from user.models import User
from django.contrib.auth.models import User as DjangoUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:

        model = User
        fields = ['username', 'password', 'email']

        
    def create(self, validated_data):

            user = User(
                email=validated_data['email'],
                username=validated_data['username']
            )
            user.set_password(validated_data['password'])
            user.save()
            return user