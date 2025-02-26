from django.urls import path, include
from rest_framework.routers import DefaultRouter
from main.views import (
    EmployeeViewSet,
    SalaryViewSet,
    CreditViewSet,
    RepaymentViewSet,
    WageViewSet,
    InputViewSet,
    BatchPriceViewSet,
    FarmViewSet,
    OwnerViewSet,
    ServicesViewSet,
    OutputViewSet,
    ToolViewSet,
    CostViewSet)

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'salary', SalaryViewSet)
router.register(r'credit', CreditViewSet)
router.register(r'repayment', RepaymentViewSet)
router.register(r'wage', WageViewSet)
router.register(r'input', InputViewSet)
router.register(r'batch_price', BatchPriceViewSet)
router.register(r'farm', FarmViewSet)
router.register(r'owner', OwnerViewSet)
router.register(r'services', ServicesViewSet)
router.register(r'output', OutputViewSet)
router.register(r'tool', ToolViewSet)
router.register(r'cost', CostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
