from grace_forte_app.services import EmployeeHierarchyService
from .BaseImportViews import *



# Create your views here.
@api_view(['GET'])
def GetEmployeeHierarchies(request):
    try:
        employeeHierarchies = EmployeeHierarchyService.GetEmployeeHierarchies()
        return Response({"Message": "Success", "Status": status.HTTP_200_OK, "Payload": employeeHierarchies.data})
    
    except Exception as ex:
        print(ex)
        return Response({"Message": ex, "Status": status.HTTP_400_BAD_REQUEST, "Payload": None})



@api_view(['GET'])
def GetEmployeeHierarchyById(request, id):
    try:
        employeeHierarchy = EmployeeHierarchyService.GetEmployeeHierarchyById(id)
        return Response({"Message": "Success", "Status": status.HTTP_200_OK, "Payload": employeeHierarchy.data})
    
    except Exception as ex:
        print(ex)
        return Response({"Message": ex.message, "Status": status.HTTP_400_BAD_REQUEST, "Payload": None})
