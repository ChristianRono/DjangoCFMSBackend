from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from main.permissions import ModelPermissions
from main.models import (
    Employee,
    Salary,
    Credit,
    Repayment,
    Wage,
    Input,
    BatchPrice,
    Farm,
    Owner,
    Services,
    Output,
    Tool,
    Cost)
from main.serializers import (
    RegisterSerializer,
    EmployeeSerializer,
    SalarySerializer,
    CreditSerializer,
    RepaymentSerializer,
    WageSerializer,
    InputSerializer,
    BatchPriceSerializer,
    FarmSerializer,
    OwnerSerializer,
    ServicesSerializer,
    OutputSerializer,
    ToolSerializer,
    CostSerializer)

class BaseModelViewSet(viewsets.ModelViewSet):
    permission_classes = [ModelPermissions]

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Generate JWT tokens
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        return Response({
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
            },
            "tokens": {
                "refresh": str(refresh),
                "access": access_token
            }
        })

class EmployeeViewSet(BaseModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]

class SalaryViewSet(BaseModelViewSet):
    queryset = Salary.objects.all()
    serializer_class = SalarySerializer
    permission_classes = [IsAuthenticated]

class CreditViewSet(BaseModelViewSet):
    queryset = Credit.objects.all()
    serializer_class = CreditSerializer
    permission_classes = [IsAuthenticated]

class RepaymentViewSet(BaseModelViewSet):
    queryset = Repayment.objects.all()
    serializer_class = RepaymentSerializer
    permission_classes = [IsAuthenticated]

class WageViewSet(BaseModelViewSet):
    queryset = Wage.objects.all()
    serializer_class = WageSerializer
    permission_classes = [IsAuthenticated]

class InputViewSet(BaseModelViewSet):
    queryset = Input.objects.all()
    serializer_class = InputSerializer
    permission_classes = [IsAuthenticated]

class BatchPriceViewSet(BaseModelViewSet):
    queryset = BatchPrice.objects.all()
    serializer_class = BatchPriceSerializer
    permission_classes = [IsAuthenticated]

class FarmViewSet(BaseModelViewSet):
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer
    permission_classes = [IsAuthenticated]

class OwnerViewSet(BaseModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
    permission_classes = [IsAuthenticated]

class ServicesViewSet(BaseModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
    permission_classes = [IsAuthenticated]

class OutputViewSet(BaseModelViewSet):
    queryset = Output.objects.all()
    serializer_class = OutputSerializer
    permission_classes = [IsAuthenticated]

class ToolViewSet(BaseModelViewSet):
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer
    permission_classes = [IsAuthenticated]

class CostViewSet(BaseModelViewSet):
    queryset = Cost.objects.all()
    serializer_class = CostSerializer
    permission_classes = [IsAuthenticated]