from django.shortcuts import render
from grace_forte_app.models.TrainingPaymentModel import TrainingPayment



# Create your Views here
def pending_payments(request):
    try:
          pending_list = TrainingPayment.objects.filter(isDeleted=False, isApproved=False)
          return render(request, "admin/transactions/pending-payments.html", {"bookingPayments": pending_payments})
    except Exception as ex:
        print(ex)



def PendingPaymentsPartial(request):
    access_token = request.session.get('access_token')
    if access_token is not None:
        response = ApiHelper.GetPendingBookingPayments(access_token)
        if response.get('detail') is not None:
            for key in list(request.session.keys()):
                del request.session[key]
            return redirect('the_admin:login')      
        
        result = TimeSinceFormatter(response['Payload'])
        
        content = {"bookingPayments": response['Payload']}
        return render(request, 'admin/transactions/_pendingPaymentList.html', content)
    
    return redirect('the_admin:login')      




# def ApprovedPayments(request):
#     access_token = request.session.get('access_token')
#     if access_token is not None:
#         response = ApiHelper.GetApprovedBookingPayments(access_token) 
#         if response.get('detail') is not None:
#             for key in list(request.session.keys()):
#                 del request.session[key]
#             return redirect('the_admin:login')      
        
#         result = ApprovedDateTimesinceFormatter(response['Payload'])
        
#         content = {"bookingPayments": response['Payload']}
#         return render(request, 'admin/transactions/approvedPayments.html', content)
#     return redirect('the_admin:login')   



# @csrf_exempt
# def ApprovePayment(request):
    received_json_data = json.loads(request.body)
    received_json_data['confirmedBy'] = request.session.get('userId')
    
    access_token = request.session.get('access_token')
    if access_token is not None:
        response = ApiHelper.ApprovePendingPayment(access_token, received_json_data)
        if response.get('detail') is not None:
            for key in list(request.session.keys()):
                del request.session[key]
                
            return redirect('the_admin:login')     
            
        data = {"Message": "Transaction Approved SuccessFully"}
        return JsonResponse(data, safe=False)
    
    return redirect('the_admin:login')     