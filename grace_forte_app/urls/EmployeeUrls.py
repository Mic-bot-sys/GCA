from django.urls import path
from grace_forte_app.views.EmployeeViews import *


urlpatterns = [
    path('get/', GetEmployees, name="get_employees"),
    path('get/<str:id>/', GetEmployeeById, name="get_employee"),
    path('post', CreateEmployee, name="create_employee"),
    path('put/<str:id>', UpdateEmployee, name="update_employee"),
    path('delete/<str:id>', DeleteEmployee, name="delete_employee"),
]