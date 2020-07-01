from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.models import apiModel
from .serializers import apiSerializer

@api_view(('GET',))
def apiView(request):
    data = {}

    if request.method == "GET":
        n = request.GET['q']

    a = apiModel.objects.get(name = n )

    data["status"] = "This is a django api"
    data["name"] = a.name
    data["phone number"] = a.phone
    data["email"] = a.email
    return Response(data)

@api_view(('GET',))
def serialView(request):
    s = apiModel.objects.all()
    serializer = apiSerializer(s, many=True)
    return Response(serializer.data)