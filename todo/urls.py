from django.urls import path
from .views import ToDoAllView, CreateToDoView, UpdateToDoView, DeleteToDoView, IndexToDoView, StatusToDoView

urlpatterns = [
    path('all/', ToDoAllView.as_view()),
    path('create/', CreateToDoView.as_view()),
    path('update/<int:task_id>', UpdateToDoView.as_view()),
    path('delete/<int:task_id>', DeleteToDoView.as_view()),
    path('index/<int:task_id>', IndexToDoView.as_view()),
]
