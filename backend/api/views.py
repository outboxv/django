from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from base.models import Stores
from .serializers import StoresSerializer


def front(request):
    context = { }
    return render(request, "index.html", context)

@api_view(['GET'])
def getStores(request):
   # param={'name':'Denis','age':28}
    slist=Stores.objects.all()
    param=StoresSerializer(slist,many=True)
    #return Response(param)
    return Response(param.data)

@api_view(['POST'])
def addStore(request):
    sz=StoresSerializer(data=request.data)
    if sz.is_valid():
        sz.save()
    return Response(sz.data)