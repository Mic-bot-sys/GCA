from django.urls import path
from grace_forte_app.views import ServicesViews

app_name = "services"

urlpatterns = [
    path('', ServicesViews.services, name="services"),
    path('details/<str:id>/', ServicesViews.service_details, name="service-details"),
    path('book/<str:id>/', ServicesViews.service_booking, name="service-bookings"),
]