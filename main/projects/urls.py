from rest_framework import routers
from django.urls import path, include

from .api import *
       
router = routers.DefaultRouter()
router.register('api/reportConfirm', ReportConfirmAPI, basename='reportConfirm')
router.register('api/financialInfos', FinancialInfoAPI, basename='financialInfo')
router.register('api/hses', HseAPI, basename='hse')
router.register('api/progressStates', ProgressStateAPI, basename='progressState')
router.register('api/timeProgressStates', TimeProgressStateAPI, basename='progressState')
router.register('api/invoices', InvoiceAPI, basename='invoice')
router.register('api/financialInvoices', FinancialInvoiceAPI, basename='financialInvoice')
router.register('api/workVolumes', WorkVolumeAPI, basename='workVolume')
router.register('api/pmsProgresses', PmsprogressAPI, basename='pmsProgress')
router.register('api/budgetCosts', BudgetCostAPI, basename='budgetCost')
router.register('api/machineries', MachineryAPI, basename='machinery')
router.register('api/projectPersonals', ProjectPersonalAPI, basename='projectPersonal')
router.register('api/problems', ProblemAPI, basename='problem')
router.register('api/criticalActions', CriticalActionAPI, basename='criticalAction')

urlpatterns = [
    path('api/reportDates', ReportDateAPIEx.as_view()),
]

urlpatterns += router.urls

