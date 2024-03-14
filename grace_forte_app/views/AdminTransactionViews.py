from datetime import datetime
from django.http import JsonResponse
from django.shortcuts import render
from grace_forte_app.models.TrainingPaymentModel import TrainingPayment
from django.contrib.auth.decorators import login_required 
from django.conf import settings
login_url = settings.ADMIN_LOGIN_URL



# Create your Views
@login_required(login_url=login_url)
def pending_training_payments(request):
    try:
        pending_transactions = TrainingPayment.objects.filter(isDeleted=False, isApproved=False).order_by("-dateCreated")[:10]
        return render(request, "admin/transactions/pending-trainings-payments.html", {"pending_transactions": pending_transactions})
    except Exception as ex:
        print(ex)



@login_required(login_url=login_url)
def pending_training_payment_details(request, id):
    try:
        pending_transaction = TrainingPayment.objects.filter( Id=id, isDeleted=False, isApproved=False).first()
        return render(request, "admin/transactions/_pending-training-payment-details.html", {"pending_transaction": pending_transaction})
    except Exception as ex:
        print(ex)



@login_required(login_url=login_url)
def approved_training_payments(request):
    try:
        approved_transactions = TrainingPayment.objects.filter(isDeleted=False, isApproved=True).order_by("-approvedDate")[:10]
        return render(request, "admin/transactions/approved-trainings-payments.html", {"approved_transactions": approved_transactions})
    except Exception as ex:
        print(ex)
        
        
    
@login_required(login_url=login_url)
def approved_training_payment_details(request, id):
    try:
        approved_transaction = TrainingPayment.objects.filter( Id=id, isDeleted=False, isApproved=True).first()
        return render(request, "admin/transactions/_approved-training-payment-details.html", {"approved_transaction": approved_transaction})
    except Exception as ex:
        print(ex)
        
        
@login_required(login_url=login_url)
def approve_training_payment(request, id):
    try:
        transaction = TrainingPayment.objects.get(pk=id)
        transaction.paymentStatus = "Approved"
        transaction.isApproved = True
        transaction.approvedBy_id = request.user.id
        transaction.approvedDate = datetime.now()
        transaction.save()
        return JsonResponse({"message": "Transaction Approved Successfully", "status": "200"})
    except Exception as ex:
        print(ex)