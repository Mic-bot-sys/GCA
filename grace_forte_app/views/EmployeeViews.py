from grace_forte_app.services import EmployeeService
from .BaseImportViews import *



# Create your views here.
@api_view(['GET'])
def GetEmployees(request):
    try:
        employees = EmployeeService.GetEmployees()
        return Response({"Message": "Success", "Status": status.HTTP_200_OK, "Payload": employees.data})
    
    except Exception as ex:
        print(ex)
        return Response({"Message": ex, "Status": status.HTTP_400_BAD_REQUEST, "Payload": None})



@api_view(['GET'])
def GetEmployeeById(request, id):
    try:
        employee = EmployeeService.GetEmployeeById(id)
        return Response({"Message": "Success", "Status": status.HTTP_200_OK, "Payload": employee.data})
    
    except Exception as ex:
        print(ex)
        return Response({"Message": ex.message, "Status": status.HTTP_400_BAD_REQUEST, "Payload": None})



@csrf_exempt
@api_view(['POST'])
def CreateEmployee(request):
    try:
        received_json_data = request.data
        employee = EmployeeService.CreateEmployee(received_json_data)
        return Response({"Message": "Success", "Status": status.HTTP_200_OK, "Payload": employee.data})
    
    except Exception as ex:
        print(ex)
        return Response({"Message": ex, "Status": status.HTTP_400_BAD_REQUEST, "Payload": None})
    


@csrf_exempt
@api_view(['PUT'])
def UpdateEmployee(request, id):
    try:
        received_json_data = request.data
        employee = EmployeeService.UpdateEmployee(id, received_json_data)
        return Response({"Message": "Success", "Status": status.HTTP_200_OK, "Payload": employee.data})
    
    except Exception as ex:
        print(ex)
        return Response({"Message": ex, "Status": status.HTTP_400_BAD_REQUEST, "Payload": None})
    


@csrf_exempt
@api_view(['DELETE'])
def DeleteEmployee(request, id):
    try:
        received_json_data = request.data
        employee = EmployeeService.DeleteEmployee(id, received_json_data)
        return Response({"Message": "Success", "Status": status.HTTP_200_OK, "Payload": employee})
    
    except Exception as ex:
        print(ex)
        return Response({"Message": ex, "Status": status.HTTP_400_BAD_REQUEST, "Payload": None})
    