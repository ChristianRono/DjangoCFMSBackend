from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    id_number = models.IntegerField()
    date_of_entry = models.DateField()
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Salary(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.DO_NOTHING)
    amount = models.FloatField()
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Salary for {self.employee.__str__}"
    
class Credit(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.DO_NOTHING)
    amount = models.FloatField()
    reason = models.TextField()
    repayment_period = models.IntegerField()
    mpesa_code = models.CharField(max_length=20)
    paid_by = models.CharField(max_length=100)
    date = models.DateField()
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Credit for {self.employee.__str__} on {str(self.date)}"
    
class Repayment(models.Model):
    credit = models.ForeignKey(Credit,on_delete=models.DO_NOTHING)
    amount = models.FloatField()
    date = models.DateField()
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Repayment for {str(self.credit)} on {str(self.date)}"
    
class Wage(models.Model):
    name = models.CharField(max_length=100)
    service = models.CharField(max_length=100)
    days = models.FloatField()
    amount = models.FloatField()
    total = models.FloatField()
    date = models.DateField()
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}, {str(self.date)}"

class Farm(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Owner(models.Model):
    name = models.CharField(max_length=100)
    farm = models.ForeignKey(Farm, on_delete=models.DO_NOTHING)
    no_of_trees = models.IntegerField()
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.farm}"

class BatchPrice(models.Model):
    description = models.TextField()
    price = models.FloatField()
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description

class Input(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=100)
    batch_price = models.ForeignKey(BatchPrice, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()
    amount = models.FloatField()
    ownership = models.ForeignKey(Owner,on_delete=models.DO_NOTHING)
    paid_by = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Services(models.Model):
    description = models.TextField()
    owner = models.ForeignKey(Owner, on_delete=models.DO_NOTHING)
    rate = models.FloatField()
    amount = models.FloatField()
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description

class Output(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.DO_NOTHING)
    tins = models.FloatField()
    rate = models.FloatField()
    amount = models.FloatField()
    date = models.DateField()
    weight = models.FloatField()
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{str(self.owner)}'s harvest for {str(self.date)}"

class Tool(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.IntegerField()
    amount = models.FloatField()
    paid_by = models.CharField()
    returned = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Cost(models.Model):
    input_ = models.ManyToManyField(Input)
    description = models.TextField()
    amount = models.FloatField()
    date = models.DateField()
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description