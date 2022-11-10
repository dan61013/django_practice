from rest_framework import serializers
from .models import Bboy

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