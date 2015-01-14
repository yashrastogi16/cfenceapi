from django.db import models
from django.utils.encoding import smart_unicode
from login.models import *
# Create your models here.
STATUS_CHOICES = (
	('0','Red'),
	('1','Amber'),
	('2','Green'),
	)
class cards(models.Model):
	cardnumber = models.BigIntegerField(unique=True)
	cardexpiry = models.TextField()
	cvv = models.IntegerField()
	status = models.CharField(max_length=10,choices=STATUS_CHOICES, null=False)
	cardtype = models.CharField(max_length=100)
	user = models.ForeignKey('login.user')
	def __unicode__(self):
		return smart_unicode(self.cardnumber)