from django.db import models
from django.utils.encoding import smart_unicode
from login_cfence.models import *
from cards.models import *

# Create your models here.
class transactions(models.Model):
	cardnumber = models.ForeignKey('cards.cards')
	user = models.ForeignKey('login.user')
	merchant = models.ForeignKey('login.merchant')
	bank = models.ForeignKey('login.bank')
	amount = models.BigIntegerField()
	transaction_description = models.TextField()
	transaction_date_time = models.DateTimeField(auto_now_add = True)
	def __unicode__(self):
		return smart_unicode(self.cardnumber)

class action(models.Model):
	onoff = models.BooleanField(default=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	phone = models.ForeignKey('login.user')
	cardnumber = models.ForeignKey('cards.cards')
	def __unicode__(self):
		return smart_unicode(self.onoff)