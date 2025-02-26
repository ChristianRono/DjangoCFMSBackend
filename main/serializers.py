from rest_framework import serializers
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
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def get_token(self, user):
        token = super().get_token(user)
        token['permissions'] = list(user.get_all_permissions())  # Include permissions
        return token


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class SalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Salary
        fields = '__all__'

class CreditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credit
        fields = '__all__'

class RepaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repayment
        fields = '__all__'

class WageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wage
        fields = '__all__'

class InputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Input
        fields = '__all__'

class BatchPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BatchPrice
        fields = '__all__'

class FarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farm
        fields = '__all__'

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'

class OutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Output
        fields = '__all__'

class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields = '__all__'

class CostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cost
        fields = '__all__'