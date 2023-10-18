from rest_framework import routers
from django.urls import path, include

from .api import *
       
router = routers.DefaultRouter()
router.register('api/hseReportDox', HseReportDoxAPI, basename='hseReportDox')

urlpatterns = [
    path('api/hseReportDox/contractList/<int:contract_id>/', HseReportDoxAPI.as_view({"get": "contractList"})),    
    path('api/hseReportDox/download/<int:id>/', HseReportDoxAPI.as_view({"get": "download"})),    
]

urlpatterns += router.urls

