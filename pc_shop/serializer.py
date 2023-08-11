from rest_framework import serializers
from .models import PCModel


class PCSerializers(serializers.ModelSerializer):
    class Meta:
        model = PCModel
        fields = '__all__'

