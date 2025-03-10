from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User
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

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def get_token(self, user):
        token = super().get_token(user)
        token['permissions'] = list(user.get_all_permissions())  # Include permissions
        return token

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class SalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Salary
        fields = '__all__'
        depth = 1

class CreditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credit
        fields = '__all__'
        depth = 1

class RepaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repayment
        fields = '__all__'
        depth = 1

class WageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wage
        fields = '__all__'

class InputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Input
        fields = '__all__'
        depth = 2

class BatchPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BatchPrice
        fields = '__all__'
        depth = 1

class FarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farm
        fields = '__all__'

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'
        depth = 1

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'
        depth = 1

class OutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Output
        fields = '__all__'
        depth = 1

class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields = '__all__'

class CostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cost
        fields = '__all__'
        depth = 1