from django.urls import path

from grace_forte_app.views.UserViews import *

urlpatterns = [
    path('get/', GetUsers, name="get_planTypes"),
    path('get/<int:id>/', GetUser, name="get_planType"),
]