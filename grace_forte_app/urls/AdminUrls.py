from django.urls import path
from grace_forte_app.views.AdminAuthViews import admin_login
from grace_forte_app.views.AdminDashboardViews import dashboard
from grace_forte_app.views.AdminTransactionViews import *

app_name = "the_admin"

urlpatterns = [
    path('', admin_login, name="admin_auth"),
    
    path('dashboard/', dashboard, name="dashboard"),
    path('pending/', pending_training_payments, name="pending-training-payments"),
    path('pending/<str:id>/', pending_training_payment_details, name="pending-training_payment-details"),
    path('approved/', approved_training_payments, name="approved-training-payments"),
    path('approved/<str:id>/', approve_training_payment, name="approve-training-payment"),
    path('approved/get/<str:id>/', approved_training_payment_details, name="approve-training-payment-details"),
    # path('approved/', dashboard, name="allServicesRendered"),
    # path('register', register, name="register"),
    # path('logout', logoutUser, name="logout"),
]