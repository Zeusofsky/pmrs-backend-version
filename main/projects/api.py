# from django.http import Http404
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, FormParser
from django.db.models import Max
# from django.db.models.functions import Substr
from datetime import datetime

from contracts.models import *
from contracts.services import GregorianToShamsi
from projects.models import *
from .serializers import *




       
