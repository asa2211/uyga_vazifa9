from rest_framework import serializers
from .models import SubjectModel


class SubjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = SubjectModel
        fields = '__all__'
