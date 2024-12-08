from django.urls import path
from . import views

app_name = 'groups'

urlpatterns = [
    path('list/', views.group_list, name='list'),
    path('group/add/', views.group_add, name='add'),
    path('group/detail/<int:pk>/', views.group_detail, name='detail'),
    path('group/delete/<int:pk>/', views.group_delete, name='delete')
]