from django.contrib import admin
from .models import ToDoModel


class ToDoAmin(admin.ModelAdmin):
    list_display = ('Task_name', 'Created_at', 'Done', 'Updated_at')
    search_fields = ('Done',)


admin.site.register(ToDoModel, ToDoAmin)
