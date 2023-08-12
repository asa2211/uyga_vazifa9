from django.urls import path
from .views import SubjectAllView, DetailSubjectView, EmailSubjectView, SearchView, CreateSubjectView, UpdateSubjectView

urlpatterns = [
    path('all/', SubjectAllView.as_view()),
    path('<int:sub_id>', DetailSubjectView.as_view()),
    path('get_email/<str:sub_email>', EmailSubjectView.as_view()),
    path('search/', SearchView.as_view()),
    path('create', CreateSubjectView.as_view()),
    path('update/<int:sub_id>', UpdateSubjectView.as_view())
]
