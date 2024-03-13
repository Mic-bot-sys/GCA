from django.urls import path
from grace_forte_app.views.AdminAuthViews import admin_login
from grace_forte_app.views.AdminDashboardViews import dashboard
from grace_forte_app.views.AdminTransactionViews import pending_payments


app_name = "the_admin"

urlpatterns = [
    path('', admin_login, name="admin_auth"),
    
    path('dashboard/', dashboard, name="dashboard"),
    path('pending/', pending_payments, name="pending"),
    path('approved/', dashboard, name="approved"),
    path('approved/', dashboard, name="allServicesRendered"),
    # path('register', register, name="register"),
    # path('logout', logoutUser, name="logout"),
]