from django.urls import path
from .views import CreatePcView, DeletePCView, PCAllView, UpdatePCView, DetailPCView, SearchView

urlpatterns = [
    path('all/', PCAllView.as_view()),
    path('create/', CreatePcView.as_view()),
    path('update/<int:pc_id>', UpdatePCView.as_view()),
    path('index/<int:pc_id>', DetailPCView.as_view()),
    path('delete/<int:pc_id>', DeletePCView.as_view()),
    path('search/', SearchView.as_view()),
]
