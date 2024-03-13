from django.urls import path

from grace_forte_app.views.HierarchyViews import *

urlpatterns = [
    path('get/', GetHierarchies, name="get_hierarchies"),
    path('get/<str:id>/', GetHierarchy, name="get_hierarchy"),
    path('post', CreateHierarchy, name="create_hierarchy"),
    path('put/<str:id>', UpdateHierarchy, name="update_hierarchy"),
    path('delete/<str:id>', DeleteHierarchy, name="delete_hierarchy"),
]