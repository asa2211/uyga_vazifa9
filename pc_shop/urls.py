from django.urls import path
from .views import CreatePcView, DeletePCView, PCAllView, UpdatePCView, DetailPCView, SearchView, SearchByCategoryView

urlpatterns = [
    path('all/', PCAllView.as_view()),
    path('create/', CreatePcView.as_view()),
    path('update/<int:pk>', UpdatePCView.as_view()),
    path('index/<int:pk>', DetailPCView.as_view()),
    path('delete/<int:pk>', DeletePCView.as_view()),
    path('search/', SearchView.as_view()),
    path('searchbycategory/<str:category_name>', SearchByCategoryView.as_view()),
]
