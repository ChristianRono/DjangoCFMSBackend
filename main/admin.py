from django.contrib import admin
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

# Register your models here.
admin.site.register(Employee)
admin.site.register(Salary)
admin.site.register(Credit)
admin.site.register(Repayment)
admin.site.register(Wage)
admin.site.register(Input)
admin.site.register(BatchPrice)
admin.site.register(Farm)
admin.site.register(Owner)
admin.site.register(Services)
admin.site.register(Output)
admin.site.register(Tool)
admin.site.register(Cost)