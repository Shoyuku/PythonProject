from django.conf.urls import url
from prediction import views

urlpatterns = [
    url(r'^predict/$', views.predict),
    url(r'^individuals/$' , views.individual_list ),
    url(r'^individual/(?P<pk>[0-9]+)/$' , views.individual_detail),
]
