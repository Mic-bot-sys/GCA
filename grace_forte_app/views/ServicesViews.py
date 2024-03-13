from django.shortcuts import redirect, render
from grace_forte_app.models.ServiceRenderedModel import ServiceRendered



# Create your Views
def services(request):
    services = ServiceRendered.objects.filter(isDeleted=False)
    return render(request, "pages/services.html", {"services": services})




def service_details(request, id):
    service = ServiceRendered.objects.get(pk=id)
    return render(request, "pages/services-details.html", {"service": service})




def service_booking(request, id):
    if request.user.is_authenticated:
        return render(request, "pages/services-booking.html")
    return redirect("authentication:auth")