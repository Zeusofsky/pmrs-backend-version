import mimetypes
from django.http import FileResponse
from django.db.models import Max, Q
from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, action, permission_classes
from rest_framework.parsers import MultiPartParser, FormParser

from projects_files.models import *
from projects_files.serializers import *


class HseReportDoxAPI(viewsets.ModelViewSet):
    queryset = HseReportDox.objects.all()
    serializer_class = HseReportDoxSerializers
    permission_classes = [
        permissions.IsAuthenticated
    ]
    parser_classes = [MultiPartParser, FormParser]

    @action(detail=True, methods=['get'])
    def contractList(self, request, *args, **kwargs):
        try:
            contractId = int(kwargs["contract_id"])
            hseReportDox = HseReportDox.objects.filter(contractid__exact=contractId)
            serializer = HseReportDoxSerializers(instance=hseReportDox, many=True)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": "error", "data": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['get'])
    def download(self, request, *args, **kwargs):
        try:
            id = int(kwargs["id"])
            hseReportDox = HseReportDox.objects.get(pk=id)
            if hseReportDox.file:
                storage, path = hseReportDox.file.storage, hseReportDox.file.path
                mimetype, _ = mimetypes.guess_type(hseReportDox.file.path)
                # file_handle = hseReportDox.file.open(path)
                response = FileResponse(storage.open(path, 'rb'), content_type=mimetype)
                response['Content-Length'] = hseReportDox.file.size
                response['Content-Disposition'] = "attachment; filename={}".format(hseReportDox.filename)
                return response    
            return Response({"status": "error", "data": "file not exist" }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            return Response({"status": "error", "data": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    
