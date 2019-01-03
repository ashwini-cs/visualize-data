from django.conf.urls import patterns, url

urlpatterns = patterns('agri_data.views',
                       url(r'^store-data$', 'store'),
