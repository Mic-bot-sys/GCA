from grace_forte_app.services import HierarchyService
from .BaseImportViews import *



# Create your views here.
@api_view(['GET'])
def GetHierarchies(request):
    try:
        hierarchies = HierarchyService.GetHierarchies()
        return Response({"Message": "Success", "Status": status.HTTP_200_OK, "Payload": hierarchies.data})
    
    except Exception as ex:
        print(ex)
        return Response({"Message": ex, "Status": status.HTTP_400_BAD_REQUEST, "Payload": None})



@api_view(['GET'])
def GetHierarchy(request, id):
    try:
        hierarchy = HierarchyService.GetHierarchyById(id)
        return Response({"Message": "Success", "Status": status.HTTP_200_OK, "Payload": hierarchy.data})
    
    except Exception as ex:
        print(ex)
        return Response({"Message": ex.message, "Status": status.HTTP_400_BAD_REQUEST, "Payload": None})



@csrf_exempt
@api_view(['POST'])
def CreateHierarchy(request):
    try:
        received_json_data = request.data
        hierarchy = HierarchyService.CreateHierarchy(received_json_data)
        return Response({"Message": "Success", "Status": status.HTTP_200_OK, "Payload": hierarchy.data})
    
    except Exception as ex:
        print(ex)
        return Response({"Message": ex, "Status": status.HTTP_400_BAD_REQUEST, "Payload": None})
    


@csrf_exempt
@api_view(['PUT'])
def UpdateHierarchy(request, id):
    try:
        received_json_data = request.data
        hierarchy = HierarchyService.UpdateHierarchy(id, received_json_data)
        return Response({"Message": "Success", "Status": status.HTTP_200_OK, "Payload": hierarchy.data})
    
    except Exception as ex:
        print(ex)
        return Response({"Message": ex, "Status": status.HTTP_400_BAD_REQUEST, "Payload": None})
    


@csrf_exempt
@api_view(['DELETE'])
def DeleteHierarchy(request, id):
    try:
        hierarchy = HierarchyService.DeleteHierarchy(id)
        return Response({"Message": "Success", "Status": status.HTTP_200_OK, "Payload": hierarchy})
    
    except Exception as ex:
        print(ex)
        return Response({"Message": ex, "Status": status.HTTP_400_BAD_REQUEST, "Payload": None})
    