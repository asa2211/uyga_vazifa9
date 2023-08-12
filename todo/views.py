from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework.views import APIView
from .models import ToDoModel
from .serializer import ToDoSerializers


class ToDoAllView(APIView):
    def get(self, *args, **kwargs):
        all = ToDoModel.objects.all()
        serializer = ToDoSerializers(all, many=True)
        return Response(serializer.data)


class CreateToDoView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ToDoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors)


class UpdateToDoView(APIView):
    def patch(self, request, *args, **kwargs):
        all = get_object_or_404(ToDoModel, id=kwargs['task_id'])
        serializer = ToDoSerializers(all, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors)


class DeleteToDoView(APIView):
    def delete(self, request, *args, **kwargs):
        all = get_object_or_404(ToDoModel, id=kwargs['task_id'])
        all.delete()
        return Response({'msg': 'deleted'})


class IndexToDoView(APIView):
    def get(self, *args, **kwargs):
        task_id = kwargs['task_id']
        ToDo = get_object_or_404(ToDoModel, id=task_id)
        serializer = ToDoSerializers(ToDo)
        return Response(serializer.data)

class StatusToDoView(APIView):
    def get(self, *args, **kwargs):
        task_status = kwargs['task_status']
        ToDo = get_object_or_404(ToDoModel, created_at=task_status.year)
        serializer = ToDoSerializers(ToDo)
        return Response(serializer.data)
