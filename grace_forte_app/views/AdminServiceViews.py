from datetime import datetime
import json
import random
from django.http import JsonResponse
from django.shortcuts import render
from grace_forte_app.models.ServicePaymentModel import ServicePayment
from grace_forte_app.models.ServiceRenderedModel import ServiceRendered
from grace_forte_app.models.TrainingPaymentModel import TrainingPayment
from django.contrib.auth.decorators import login_required 
from django.conf import settings
login_url = settings.ADMIN_LOGIN_URL


        
# Create the Views here
@login_required(login_url=login_url)
def create_service(request):
    try:
        if request.method == "GET":
            return render(request, "admin/service/create-service.html")
        
        body = json.loads(request.body)
    except Exception as ex:
        print(ex)
        
        
        
@login_required(login_url=login_url)
def services(request):
    try:
        if request.method == "GET":            
            services = ServiceRendered.objects.filter(isDeleted=False)
            return render(request, "admin/service/services.html", {"services": services})
    except Exception as ex:
        print(ex)
        
        