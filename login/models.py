from django.db import models
from django.utils.encoding import smart_unicode

class user(models.Model):
	phone = models.CharField(unique=True,max_length=20)
	pin = models.IntegerField()
	address = models.CharField(max_length=250)
	name = models.CharField(max_length=60, null=True)
	email = models.EmailField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return smart_unicode(self.id)

class merchant(models.Model):
	name = models.CharField(max_length=100)
	userid = models.CharField(max_length=100, unique=True)
	phone = models.CharField(unique=True,max_length=20)
	password = models.CharField(max_length=20)
	email = models.EmailField()
	created_at = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return smart_unicode(self.name)
		
class bank(models.Model):
	username = models.CharField(unique=True,max_length=100)
	password = models.CharField(max_length=100)
	bankname = models.CharField(max_length=100)
	address = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return smart_unicode(self.username)