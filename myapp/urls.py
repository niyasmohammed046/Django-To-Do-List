from django.urls import path
from . import views

urlpatterns = [

    path('',views.home,name='home'),
    path('addtask/',views.addtask,name="addtask"),
    path('done/<int:pk>/',views.MarkAsDone,name="MarkAsDone"),
    path('undone/<int:pk>/',views.MarkAsUnDone,name="MarkAsUnDone"),
    path('edit/<int:pk>/',views.edit,name="edit"),
    path('delete/<int:pk>/',views.deletetask,name="delete_task")
]