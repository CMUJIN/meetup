import json

from django.core import serializers
from django.http import Http404
from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from api.models import Account, Match, Location
from api.serializers import AccountSerializer, MatchSerializer, \
    LocationSerializer


def get_account_object(pk):
    try:
        return Account.objects.get(pk=pk)
    except Account.DoesNotExist:
        raise Http404
    
def get_nearby_account(userid, latitude, longitude):
    try:
        return Location.objects.filter(latitude=latitude, longitude=longitude).exclude(user_id=userid)
    except Location.DoesNotExist:
        return None

def get_location(pk):
    try:
        return Location.objects.get(pk=pk)
    except Location.DoesNotExist:
        return None
    
def get_match_object(userid, match_userid):
    try:
        return Match.objects.get(user_id=userid, match_user_id=match_userid)
    except Match.DoesNotExist:
        return None
    
def get_all_match_objects(userid):
    try:
        return Match.objects.filter(user_id=userid, islike=True)
    except Match.DoesNotExist:
        return None
    
def check_match_object(userid, match_userid):
    try:
        Match.objects.get(user_id=userid, match_user_id=match_userid, islike=True)
        Match.objects.get(user_id=match_userid, match_user_id=userid, islike=True)
        return True
    except Match.DoesNotExist:
        return False
@api_view(['POST'])
@csrf_exempt    
def create_account(request):
    serializer = AccountSerializer(data=request.DATA)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
@csrf_exempt
def get_account(request, pk):
    account = get_account_object(pk)
    serializer = AccountSerializer(account)
    return Response(serializer.data, status=status.HTTP_200_OK)
@api_view(['PUT'])
@csrf_exempt
def update_account(request, pk):
    account = get_account_object(pk)
    serializer = AccountSerializer(account, data=request.DATA)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['PUT'])
@csrf_exempt
def update_location(request):
    serializer = LocationSerializer(data=request.DATA)
    json_response = simplejson.loads(JSONRenderer().render(serializer.data))
    location = get_location(json_response['user_id'])
    if location != None:
        serializer = LocationSerializer(location, data=request.DATA)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@csrf_exempt
def delete_account(request, pk):
    account = get_account_object(pk)
    account.delete()
    return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
@csrf_exempt
def find_people(request, pk):
    account = get_location(pk)
    locations = get_nearby_account(pk, account.latitude, account.longitude)
    response = []
    for location in locations:
        people = get_account_object(location.user_id)
        response.append(AccountSerializer(people).data)
    return Response(response, content_type="application/json", status=status.HTTP_200_OK)

@api_view(['POST'])
@csrf_exempt
def create_match(request):
    serializer = MatchSerializer(data=request.DATA)
    json_response = simplejson.loads(JSONRenderer().render(serializer.data))
    match = get_match_object(json_response['user_id'],json_response['match_user_id'])
    if match!=None:
        serializer = MatchSerializer(match, data=request.DATA)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@csrf_exempt
def check_match(request, pk):
    user_id = pk
    match_user_id = request.GET.get('match_user_id', '')
    userMatch = get_match_object(user_id, match_user_id)
    serializer = MatchSerializer(userMatch)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@csrf_exempt
def get_all_match(request, pk):
    match_records = get_all_match_objects(pk)
    response = []
    if match_records is None:
        return Response("no available records", status=status.HTTP_204_NO_CONTENT)
    else:
        for match in match_records:
            ismatch = check_match_object(pk, match.match_user_id)
            if ismatch is True:
                data = {}
                data['user_id'] = match.match_user_id
                response.append(data)
        return Response(response, content_type="application/json", status=status.HTTP_200_OK)

