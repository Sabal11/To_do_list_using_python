from django.urls import path
from  .views import Tasklist, Taskdetail, TaskCreate, Taskupdate, Taskdelete

urlpatterns = [
    path('',Tasklist.as_view(), name = "Task"),
    path('task/<int:pk>',Taskdetail.as_view(), name = 'details'),
    path('task_create',TaskCreate.as_view(), name ='create'),
    path('task_update/<int:pk>',Taskupdate.as_view(), name = 'update'),
    path('task_delete/<int:pk>',Taskdelete.as_view(), name = 'delete')
]