from django.conf.urls import url, include
from django.contrib import admin
from views import form_view

urlpatterns = [
    url(r'^lnx/$',form_view),
]