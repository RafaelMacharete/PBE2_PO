from django.shortcuts import render
from .models import Event
from .serializers import EventSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from datetime import datetime, timedelta

'''
Filter ALL events by parameters given
Create events
'''
@api_view(['GET', 'POST'])
def get_create_events_by_params(
    req, 
    category=None,
    date=None, 
    qnt=None,
    ordering=None
    ):
    if req.method == 'GET':
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
            all_events_filtered = all_events_filtered[0:int(qnt)]

        events_serializer = EventSerializer(all_events_filtered, many=True)
        return Response(events_serializer.data, status=status.HTTP_200_OK)
    elif req.method == 'POST':
        event_serializer = EventSerializer(data=req.data)
        if event_serializer.is_valid():
            event_serializer.save()
            return Response(event_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(event_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

'''
Takes an event by pk given by parameter
Edit a event info by pk
Delete a event by pk
'''
@api_view(['GET', 'PUT', 'DELETE'])    
def alter_get_event_state(req, pk):
    if req.method == 'GET':
        try:
            event_by_pk = Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        event_by_pk_serializer = EventSerializer(event_by_pk)
        return Response(event_by_pk_serializer.data, status=status.HTTP_200_OK)
    
    elif req.method == 'PUT':
        try:
            event_by_pk = Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        event_by_pk_serializer = EventSerializer(event_by_pk, data=req.data)
        if event_by_pk_serializer.is_valid():
            event_by_pk_serializer.save()
            return Response(event_by_pk_serializer.data, status=status.HTTP_200_OK)
    elif req.method == 'DELETE':
        try:
            event_by_pk = Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        event_by_pk.delete()
        return Response('Event deleted', status=status.HTTP_204_NO_CONTENT)

# Filter events upcoming on 7 days
@api_view(['GET'])
def get_upcoming_events(req):
    # current_date = datetime.today().strftime('%Y-%m-%d')
    # current_date_object = datetime.strptime(current_date, '%Y-%m-%d')
    # seven_days_forward_of_current_date = (current_date_object + timedelta(days=7)).strftime('%Y-%m-%d')
    

    upcoming_events = Event.objects.all().filter(event_date__gt = current_date).filter(event_date__lte = seven_days_forward_of_current_date)
    upcoming_events_serializer = EventSerializer(upcoming_events, many=True)
    return Response(upcoming_events_serializer.data, status=status.HTTP_200_OK)