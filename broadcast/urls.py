from django.urls import path
from . import views


urlpatterns = [ 
    path('broadcast', views.broadcast_sms, name="default"),
]