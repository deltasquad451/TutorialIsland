'''
Created on Dec 12, 2014

@author: lando
'''
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from models import consumeRESTAPI

#We are using hyperlinked relations in this case, with HyperlinkedModelSerializer
#Hyperlinking is good RESTful design due to URI's referrring to resources
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url','username','email','groups')
        
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url','name')
        
class consumeAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = consumeRESTAPI
        fields=('urlField','getJSON')
        