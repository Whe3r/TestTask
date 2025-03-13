from django.urls import path
from .views import DepartmentTreeView

urlpatterns = [
    path('departments/', DepartmentTreeView.as_view(), name='department-tree'),
]
