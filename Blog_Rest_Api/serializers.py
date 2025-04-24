from rest_framework import serializers
from .models import  PostModel
from django.contrib.auth.models import User


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username','email','password')

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class PostSerializer(serializers.ModelSerializer):
    email = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = PostModel
        fields = ('id','title','description','post_image','email')
        read_only_fields = ['email']

    def get_email(self, obj):
        return obj.user.email if obj.user else None

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    
