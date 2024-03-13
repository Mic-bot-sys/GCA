from django.urls import path

from grace_forte_app.views.EmployeeHierarchyViews import *

urlpatterns = [
    path('get/', GetEmployeeHierarchies, name="get_employee_hierarchies"),
    path('get/<str:id>/', GetEmployeeHierarchyById, name="get_employee_hierarchy"),
]