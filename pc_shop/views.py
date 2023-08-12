from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.response import Response

from .models import PCModel, CategoryModel
from .serializer import PCSerializers
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404


class PCAllView(generics.ListAPIView):
    queryset = PCModel.objects.all()
    serializer_class = PCSerializers


class DetailPCView(generics.RetrieveAPIView):
    queryset = PCModel.objects.all()
    serializer_class = PCSerializers


class SearchView(generics.ListAPIView):
    queryset = PCModel.objects.all()
    serializer_class = PCSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'pc_name']


class CreatePcView(generics.CreateAPIView):
    queryset = PCModel.objects.all()
    serializer_class = PCSerializers


class UpdatePCView(generics.UpdateAPIView):
    queryset = PCModel.objects.all()
    serializer_class = PCSerializers


class DeletePCView(generics.DestroyAPIView):
    queryset = PCModel.objects.all()
    serializer_class = PCSerializers


class SearchByCategoryView(APIView):
    def get(self, *args, **kwargs):
        category_name = kwargs["category_name"]
        category = get_object_or_404(CategoryModel, category_name=category_name)
        pc = PCModel.objects.filter(category_id=category.id)
        serializer = PCSerializers(pc, many=True)
        return Response(serializer.data)
