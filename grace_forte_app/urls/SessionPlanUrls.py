from django.urls import path

from grace_forte_app.views.SessionPlanViews import *

urlpatterns = [
    path('get/', GetSessionPlans, name="get_sessionPlans"),
    path('get/<str:id>/', GetSessionPlan, name="get_sessionPlan"),
    path('post', CreateSessionPlan, name="create_sessionPlan"),
    path('put/<str:id>', UpdateSessionPlan, name="update_sessionPlan"),
    path('delete/<str:id>', DeleteSessionPlan, name="delete_sessionPlan"),
]