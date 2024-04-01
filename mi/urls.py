from django.urls import path
from mi.views import *
app_name='something'

urlpatterns = [
    path('rohith/',rohith,name='rohith'),
]
