from rest_framework import serializers
from .models import Bboy

class BboySerializer(serializers.ModelSerializer):
    class Meta:
        model = Bboy
        fields = '__all__'