from rest_framework.views import APIView
from .get_data_logic import data_get
from rest_framework.response import Response
# Create your views here.

class Activity(APIView):
    '''
    class for returning activityperiod
    '''
    def get(self,request):
        result=data_get()
        return Response(result)