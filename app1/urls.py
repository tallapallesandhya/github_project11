from django.urls import path
from app1.views import *
app_name='sonu'

urlpatterns=[
    path('a1_first/',a1_first,name='a1_first'),
]