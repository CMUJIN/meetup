from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Account
from api.serializers import AccountSerializer


def get_object(pk):
    try:
        return Account.objects.get(pk=pk)
    except Account.DoesNotExist:
        raise Http404

@api_view(['POST'])
@csrf_exempt    
def create(request):
    serializer = AccountSerializer(data=request.DATA)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
@csrf_exempt
def get(request, pk=123):
    account = get_object(pk)
    serializer = AccountSerializer(account)
    return Response(serializer.data, status=status.HTTP_200_OK)
@api_view(['PUT'])
@csrf_exempt
def update(request, pk):
    account = get_object(pk)
    serializer = AccountSerializer(account, data=request.DATA)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['DELETE'])
@csrf_exempt
def delete(request, pk):
    account = get_object(pk)
    account.delete()
    return Response(status=status.HTTP_200_OK)

