from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from rest_framework.status import HTTP_201_CREATED

from .models import SubjectModel
from .serializer import SubjectSerializers
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404


class SubjectAllView(APIView):
    def get(self, *args, **kwargs):
        all = SubjectModel.objects.all()
        serializer = SubjectSerializers(all, many=True)
        return Response(serializer.data)


class DetailSubjectView(APIView):
    def get(self, *args, **kwargs):
        sub_id = kwargs['sub_id']
        subject = get_object_or_404(SubjectModel, id=sub_id)
        serializer = SubjectSerializers(subject)
        return Response(serializer.data)


def get(*args, **kwargs):
    sub_email = kwargs['sub_email']
    subject = get_object_or_404(SubjectModel, email=sub_email)
    serializer = SubjectSerializers(subject)
    return Response(serializer.data)


class EmailSubjectView(APIView):
    pass


class SearchView(generics.ListAPIView):
    queryset = SubjectModel.objects.all()
    serializer_class = SubjectSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'email', 'subject_name']


class CreateSubjectView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = SubjectSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors)


class UpdateSubjectView(APIView):
    def patch(self, request, *args, **kwargs):
        subject = get_object_or_404(SubjectModel, id=kwargs['sub_id'])
        serializer = SubjectSerializers(subject, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors)
