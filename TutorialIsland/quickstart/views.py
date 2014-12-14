from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from serializers import UserSerializer, GroupSerializer, consumeAPISerializer
from models import consumeRESTAPI
"""
Rather that writing multiple views we're grouping together all the common behavior into 'viewset'
'viewsets' - allow us to break these down into individual views if we need to, but using viewsets
keeps the logic nicely organized as well as being very concise
setting the 'queryset' and/or serializer_class attributes gives you more explicit control of the API behavior
and is the reccommended style for most applications
"""
class UserViewSet(viewsets.ModelViewSet):
    """
    API Endpoint that allows users to be viewed or edited
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class GroupViewSet(viewsets.ModelViewSet):
    """
    API Endpoint that allows users to be viewed or edited
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    
class consumeViewSet(viewsets.ModelViewSet):
    """
    API Endpoint that allows users to be viewed or edited
    """
    queryset = consumeRESTAPI.objects.all()
    serializer_class = consumeAPISerializer
    
    
