from grace_forte_app.services import SessionPlanService
from .BaseImportViews import *



# Create your views here.
@api_view(['GET'])
def GetSessionPlans(request):
    try:
        sessionPlans = SessionPlanService.GetSessionPlans()
        return Response({"Message": "Success", "Status": status.HTTP_200_OK, "Payload": sessionPlans.data})
    
    except Exception as ex:
        print(ex)
        return Response({"Message": ex, "Status": status.HTTP_400_BAD_REQUEST, "Payload": None})



@api_view(['GET'])
def GetSessionPlan(request, id):
    try:
        sessionPlan = SessionPlanService.GetSessionPlanById(id)
        return Response({"Message": "Success", "Status": status.HTTP_200_OK, "Payload": sessionPlan.data})
    
    except Exception as ex:
        print(ex)
        return Response({"Message": ex.message, "Status": status.HTTP_400_BAD_REQUEST, "Payload": None})



@csrf_exempt
@api_view(['POST'])
def CreateSessionPlan(request):
    try:
        received_json_data = request.data
        sessionPlan = SessionPlanService.CreateSessionPlan(received_json_data)
        return Response({"Message": "Success", "Status": status.HTTP_200_OK, "Payload": sessionPlan.data})
    
    except Exception as ex:
        print(ex)
        return Response({"Message": ex, "Status": status.HTTP_400_BAD_REQUEST, "Payload": None})
    


@csrf_exempt
@api_view(['PUT'])
def UpdateSessionPlan(request, id):
    try:
        received_json_data = request.data
        sessionPlan = SessionPlanService.UpdateSessionPlan(id, received_json_data)
        return Response({"Message": "Success", "Status": status.HTTP_200_OK, "Payload": sessionPlan.data})
    
    except Exception as ex:
        print(ex)
        return Response({"Message": ex, "Status": status.HTTP_400_BAD_REQUEST, "Payload": None})
    


@csrf_exempt
@api_view(['DELETE'])
def DeleteSessionPlan(request, id):
    try:
        sessionPlan = SessionPlanService.DeleteSessionPlan(id)
        return Response({"Message": "Success", "Status": status.HTTP_200_OK, "Payload": sessionPlan})
    
    except Exception as ex:
        print(ex)
        return Response({"Message": ex, "Status": status.HTTP_400_BAD_REQUEST, "Payload": None})
    