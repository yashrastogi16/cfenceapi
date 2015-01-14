from django.forms import widgets
from rest_framework import serializers
from login.models import *
from cards.models import *

class userSerializer(serializers.ModelSerializer):
	class Meta:
		model = user
		fields = ('id','phone','address','name','email')

class merchantSerializer(serializers.ModelSerializer):
	class Meta:
		model = merchant
		fields = ('id','phone','userid','name','email')

class bankSerializer(serializers.ModelSerializer):
	class Meta:
		model = bank

class cardsSerializer(serializers.ModelSerializer):
	class Meta:
		model = cards