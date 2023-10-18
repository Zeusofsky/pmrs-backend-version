from rest_framework import serializers

from projects.models import *


#=========== Contract Serializers ============
class ReportDateSerializerEx(serializers.ModelSerializer):
    shamsiDate = serializers.ReadOnlyField()
    class Meta:
        model = ReportDate
        fields = ('dateid', 'shamsiDate')
        

class ReportConfirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportConfirm
        fields = '__all__'  

        
class FinancialInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialInfo
        fields = '__all__'


class HseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hse
        fields = '__all__'
        
         
class ProblemSerializer(serializers.ModelSerializer):
    # row_number = serializers.ReadOnlyField() , "row_number"
    class Meta:
        model = Problem
        fields = ("problemid", "contractid", "dateid", "problem")


class CriticalActionSerializer(serializers.ModelSerializer):
    # row_number = serializers.ReadOnlyField() , "row_number"
    class Meta:
        model = CriticalAction
        fields = ("criticalactionid", "contractid", "dateid", "criticalaction")
