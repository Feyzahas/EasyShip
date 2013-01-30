from django.conf.urls import patterns, url

from root import views

urlpatterns = patterns('',
	url(r'^$', views.search, name='search'),
	url(r'^login$', 'app.account.login'),
	url(r'^logout$', 'app.account.logout'),
	url(r'^signup$', 'app.account.signup'),
)
