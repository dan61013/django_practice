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

class RegisterSerializer(serializers.ModelSerializer):
    
    # 利用UniqueValidator，來判斷是否為唯一值
    username = serializers.CharField(
        required = True,
        validators = [UniqueValidator(queryset=User.objects.all())]
    )
    
    # 使用2組password, 原因是要給使用者確認一次密碼，用validate_password來驗證兩次是否相同
    password = serializers.CharField(
        write_only = True,
        required = True,
        validators = [validate_password],
        style = {'input_type': 'password'} # input_type, 會把密碼加以屏蔽
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
    
    class Meta:
        
        # model以User為主體，UserProfile是擴充包, 但在fields一樣要記得把擴充選項新增進去
        model = User
        fields = (
            'username', 'email', 'password', 'password2', 'phone', 'instagram', 'organization'
        )
        
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password":"Password fields didn't match."})
        return attrs
    
    # 使用ORM (Object Relational Mapping) 的方式來create model instance，同時重新定義create，
    # 另一方面我們也同時create UserProfile的 instance，並對應我們創建的User instance。
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