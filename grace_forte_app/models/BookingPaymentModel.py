from grace_forte_app.models.BookingModel import Booking
from grace_forte_app.special_services.CustomDateTime import DateTime
from .BaseImportModel import *
from django.contrib.auth.models import User
from datetime import datetime

class BookingPayment(models.Model):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    paymentStatus = models.CharField(max_length=50, default="Pending")
    paymentProof = models.FileField(upload_to="payment_proof/", blank=True, null=True)
    proofBase = models.TextField()
    sessionAmount = models.IntegerField(default=1)
    totalExpectedAmount = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    approvedDate = models.DateTimeField(auto_now_add=False, blank=True, null=True )
    
    # Foreign Fields
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE, related_name='booking')
    approvedBy = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name='approvedBy')
    
    # Other Fields
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateDeleted = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    isDeletedBy = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    isDeleted = models.BooleanField(default=False)

    
    class Meta:
        verbose_name_plural = 'BookingPayments'
    
    def __str__(self):
        return self.paymentStatus
    