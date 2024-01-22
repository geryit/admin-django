# serializers.py
from rest_framework import serializers
from work.models import Work

class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = '__all__'  # You can specify fields you want to include
