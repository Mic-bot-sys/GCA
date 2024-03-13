
from django.shortcuts import render



#Create your Views here
def dashboard(request):
    return render(request, 'admin/dashboard/dashboard.html')