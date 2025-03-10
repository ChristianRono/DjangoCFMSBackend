from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from main.views import (
    RegisterView,
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
from main.serializers import CustomTokenObtainPairSerializer

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
    path('register/', RegisterView.as_view(), name='register'),
    path('api/token/', TokenObtainPairView.as_view(serializer_class = CustomTokenObtainPairSerializer), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
