from django.shortcuts import render
from serializers import *
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from login.models import *
from cards.models import *

# Create your views here.

# API for user login.
@api_view(['GET','POST'])
def user_login(request):
	try:
		user1 = user.objects.all()
	except user1.DoesNotExist:
		return Response(status = status.HTTP_404_NOT_FOUND)
	if request.method =='GET':
		serializer = userSerializer(user1, many = True)
		return Response(serializer.data)

	if request.method == 'POST':
		data = {}
		result = {}
		phone = request.POST['username']
		pin = request.POST['password']
		a = str(phone)
		b = str(pin)
		user_obj = user.objects.filter(phone = a, pin=b)
		if user_obj:
			userobj = user_obj[0]
			request.session['user']=userobj.id
			data['phone'] = userobj.phone
			data['username'] = userobj.name
			result['code'] = 1
			result['message'] = 'Success'
			result['session'] = request.session['user']
			result['data'] = data
		return Response(result)

# API for Merchant login.
@api_view(['GET','POST'])
def merchant_login(request):
	try:
		merchant1 = merchant.objects.all()
	except merchant1.DoesNotExist:
		return Response(status = status.HTTP_404_NOT_FOUND)
	if request.method =='GET':
		serializer = merchantSerializer(merchant1, many = True)
		return Response(serializer.data)
	if request.method == 'POST':
		data = {}
		result = {}
		userid = request.POST['userid']
		password = request.POST['password']
		a = str(userid)
		b = str(password)
		try:
			merchant_obj = merchant.objects.filter(userid = a, password=b)
		except:
			print "Error"
		if merchant_obj:
			merchantobj = merchant_obj[0]
			request.session['merchant']=merchantobj.id
			data['name'] = merchantobj.name
			data['phone'] = merchantobj.phone
			result['code'] = 1
			result['message'] = 'Success'
			result['session'] = request.session['merchant']
			result['data'] = data
		return Response(result)

# API for users cards.
@api_view(['GET','POST'])
def user_home(request):
	if request.method == 'POST':
		print 'inside post method'
		data = {}
		result = {}
		data1 = []
		userid = request.POST['userid']
		cards_obj = cards.objects.filter(user = userid)
		if cards_obj:
			for i in cards_obj:
				data['cardnumber'] = i.cardnumber
				data['cardexpiry'] = i.cardexpiry
				data['cvv'] = i.cvv
				data['status'] = i.status
				data['cardtype'] = i.cardtype
				data1.append(data)
			result['code'] = 1
			result['message'] = 'Success'
			result['data'] = data1
		return Response(result)

# API for cards status.
@api_view(['GET','POST'])
def card_status(request):
	if request.method == 'POST':
		data = {}
		result = {}
		cardnumber = request.POST['cardnumber']
		print cardnumber
		status1 = request.POST['status']
		z = int(status1)
		print type(z)
		if (z >= 0 and z <= 2):
			cards_obj = cards.objects.get(cardnumber = cardnumber)
			cards_obj.status = status1
			cards_obj.save()
			data['status'] = status1
			result['code'] = 1
			result['message'] = "Success"
			result['data'] = data
		else:
			result['code'] = 0
			result['message'] = "Error"
	return Response(result)



