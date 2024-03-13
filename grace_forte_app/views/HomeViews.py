from django.shortcuts import render
from grace_forte_app.models.TrainingPaymentModel import TrainingPayment
from django.contrib.auth.decorators import login_required



# Create your views here
def home(request):
    return render(request, "pages/index.html")



def about(request):
    return render(request, "pages/about.html")



@login_required
def pending_trainings_transaction(request):
    transactions = TrainingPayment.objects.filter(isDeleted=False, isApproved=False, user_id=request.user.id).order_by("-dateCreated")
    return render(request, "pages/pending-trainings-transaction.html", {"pending_transactions": transactions})



@login_required
def approved_trainings_transaction(request):
    transactions = TrainingPayment.objects.filter(isDeleted=False, isApproved=True, user_id=request.user.id).order_by("-approvedDate")
    return render(request, "pages/approved-trainings-transaction.html", {"approved_transactions": transactions})



def pending_bookings_transaction(request):
    return render(request, "pages/pending-bookings-transaction.html")



def contact(request):
    return render(request, "pages/contact.html")
