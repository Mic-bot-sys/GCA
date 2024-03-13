from django.shortcuts import redirect, render

from grace_forte_app.models.CourseModel import Course
from grace_forte_app.models.TrainingPaymentModel import TrainingPayment

def trainings(request):
    courses = Course.objects.filter(isDeleted=False)
    return render(request, "pages/trainings.html", {"courses": courses})


def training_details(request, id):
    course = Course.objects.get(pk=id)
    return render(request, "pages/trainings-details.html", {"course": course})


def training_enrollment(request, id):
    if request.user.is_authenticated:
        course = Course.objects.get(pk=id)
        return render(request, "pages/trainings-enrollment.html", {"course": course})
    return redirect("authentication:auth")



def approved_training_receipt(request, id):
    if request.user.is_authenticated:
        receipt = TrainingPayment.objects.filter(Id=id, isDeleted=False, isApproved=True).first()
        dateApproved = receipt.getDateApprovedOnly()
        return render(request, "receipts/approved-training-transaction-receipt.html", {"receipt": receipt, "dateApproved": dateApproved})
