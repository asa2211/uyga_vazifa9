from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.status import HTTP_201_CREATED

from .models import PCModel
from .serializer import PCSerializers
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404


class PCAllView(APIView):
    def get(self, *args, **kwargs):
        all = PCModel.objects.all()
        serializer = PCSerializers(all, many=True)
        return Response(serializer.data)


class DetailPCView(APIView):
    def get(self, *args, **kwargs):
        pc_id = kwargs['pc_id']
        pc = get_object_or_404(PCModel, id=pc_id)
        serializer = PCSerializers(pc)
        return Response(serializer.data)


class SearchView(generics.ListAPIView):
    queryset = PCModel.objects.all()
    serializer_class = PCSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'pc_name']


class CreatePcView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = PCSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors)


class UpdatePCView(APIView):
    def patch(self, request, *args, **kwargs):
        pc = get_object_or_404(PCModel, id=kwargs['pc_id'])
        serializer = PCSerializers(pc, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors)


class DeletePCView(APIView):
    def delete(self, request, *args, **kwargs):
        all = get_object_or_404(PCModel, id=kwargs["pc_id"])
        all.delete()
        return Response({'msg': 'deleted'})
