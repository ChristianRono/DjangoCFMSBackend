from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
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

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]

class SalaryViewSet(viewsets.ModelViewSet):
    queryset = Salary.objects.all()
    serializer_class = SalarySerializer
    permission_classes = [IsAuthenticated]

class CreditViewSet(viewsets.ModelViewSet):
    queryset = Credit.objects.all()
    serializer_class = CreditSerializer
    permission_classes = [IsAuthenticated]

class RepaymentViewSet(viewsets.ModelViewSet):
    queryset = Repayment.objects.all()
    serializer_class = RepaymentSerializer
    permission_classes = [IsAuthenticated]

class WageViewSet(viewsets.ModelViewSet):
    queryset = Wage.objects.all()
    serializer_class = WageSerializer
    permission_classes = [IsAuthenticated]

class InputViewSet(viewsets.ModelViewSet):
    queryset = Input.objects.all()
    serializer_class = InputSerializer
    permission_classes = [IsAuthenticated]

class BatchPriceViewSet(viewsets.ModelViewSet):
    queryset = BatchPrice.objects.all()
    serializer_class = BatchPriceSerializer
    permission_classes = [IsAuthenticated]

class FarmViewSet(viewsets.ModelViewSet):
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer
    permission_classes = [IsAuthenticated]

class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
    permission_classes = [IsAuthenticated]

class ServicesViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
    permission_classes = [IsAuthenticated]

class OutputViewSet(viewsets.ModelViewSet):
    queryset = Output.objects.all()
    serializer_class = OutputSerializer
    permission_classes = [IsAuthenticated]

class ToolViewSet(viewsets.ModelViewSet):
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer
    permission_classes = [IsAuthenticated]

class CostViewSet(viewsets.ModelViewSet):
    queryset = Cost.objects.all()
    serializer_class = CostSerializer
    permission_classes = [IsAuthenticated]