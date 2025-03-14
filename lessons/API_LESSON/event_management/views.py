from django.shortcuts import render
from .models import Event
from .serializers import EventSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET'])
def get_all_events(req):
    all_events = Event.objects.all()
    all_events_serializer = EventSerializer(all_events, many=True)
    return Response(all_events_serializer.data)

@api_view(['GET'])
def get_events_by_params(
    req, 
    category=None,
    date=None, 
    qnt=None,
    ordering=None
    ):
    category = req.query_params.get('category', None)
    date = req.query_params.get('date', None)
    qnt = req.query_params.get('qnt', None)
    ordering = req.query_params.get('ordering', None)
    

    all_events_filtered = Event.objects.all()
    if category:
        all_events_filtered = all_events_filtered.filter(event_category__icontains = category)
    if date:
        all_events_filtered = all_events_filtered.filter(event_date__icontains = date)
    if ordering:
        all_events_filtered = all_events_filtered.filter(event_date__gt = ordering)
    if qnt:
        all_events_filtered = all_events_filtered[0:qnt]

    events_serializer = EventSerializer(all_events_filtered, many=True)
    return Response(events_serializer.data, status=status.HTTP_200_OK)