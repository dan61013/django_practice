from rest_framework import serializers
from .models import Bboy, UserProfile

from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

# class BboySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Bboy
#         fields = '__all__'

class BboySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=20)
    age = serializers.IntegerField()
    power = serializers.BooleanField()
    skills = serializers.CharField(max_length=200)
    
    # 新增驗證功能
    def validate_age(self):
        if self.age < 0:
            raise serializers.ValidationError("Age must be bigger than 0!")

class RegisterSerializer(serializers.ModelField):
    
    username = serializers.CharField(
        required = True,
        validators = [UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only = True,
        required = True,
        validators = [validate_password],
        style = {'input_type': 'password'}
        )
    
    password2 = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
        )
    
    email = serializers.EmailField(write_only=True, required=True)
    phone = serializers.CharField(min_length=8, max_length=10, write_only=True)
    instagram = serializers.CharField(min_length=2, max_length=50, write_only=True)
    
    organization = serializers.CharField(max_length=100)
    
    class Mata:
        
        model = User
        fields = (
            'username', 'email', 'password', 'password2', 'phone', 'instagram', 'organization'
        )
        
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password":"Password fields didn't match."})
        return attrs
    
    def create(self, vaildated_data):
        user = User.objects.create(
            username = vaildated_data['username'],
            email = vaildated_data['email'],
            password = vaildated_data['password'],
        )

        userprofile = UserProfile.objects.create(
            user = user,
            phone = vaildated_data['phone'],
            instagram = vaildated_data['instagram'],
            organization = vaildated_data['organization'],
        )
        
        user.set_password(vaildated_data['password'])
        user.save()
        
        return user