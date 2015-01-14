from django.conf.urls import patterns, include, url
from django.contrib import admin
from api import views

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'cfence.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),
	# Url for Admin Login.
	url(r'^admin/', include(admin.site.urls)),
	# Url for Bank Login
	# Url's for API
	url(r'^user_login/','api.views.user_login',name='user_login'),
	url(r'^merchant_login/','api.views.merchant_login',name = 'merchant_login'),
	url(r'^user_home/','api.views.user_home',name='user_home'),
	url(r'^card_status/','api.views.card_status',name = 'card_status')
	)
