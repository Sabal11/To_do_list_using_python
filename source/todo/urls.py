from django.urls import path
from  .views import Tasklist, Taskdetail, TaskCreate, Taskupdate, Taskdelete, Login, Register
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',Tasklist.as_view(), name = "Task"),
    path('task/<int:pk>',Taskdetail.as_view(), name = 'details'),
    path('task_create/',TaskCreate.as_view(), name ='create'),
    path('task_update/<int:pk>',Taskupdate.as_view(), name = 'update'),
    path('task_delete/<int:pk>',Taskdelete.as_view(), name = 'delete'),
    path('login',Login.as_view(), name ='login'),
    path('login',LogoutView.as_view(), name ='logout'),
    path('register/',Register.as_view(), name ='register'),
]

