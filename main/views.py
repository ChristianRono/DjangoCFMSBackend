from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
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