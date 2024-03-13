from grace_forte_app.services import UserService
from .BaseImportViews import *



# Create your views here.
@api_view(['GET'])
def GetUsers(request):
    try:
        users = UserService.GetUsers()
        return Response({"Message": "Success", "Status": status.HTTP_200_OK, "Payload": users.data})
    
    except Exception as ex:
        print(ex)
        return Response({"Message": ex, "Status": status.HTTP_400_BAD_REQUEST, "Payload": None})



@api_view(['GET'])
def GetUser(request, id):
    try:
        user = UserService.GetUserById(id)
        return Response({"Message": "Success", "Status": status.HTTP_200_OK, "Payload": user.data})
    
    except Exception as ex:
        print(ex)
        return Response({"Message": ex.message, "Status": status.HTTP_400_BAD_REQUEST, "Payload": None})