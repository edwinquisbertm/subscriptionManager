from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=15)
    phone2 = models.CharField(max_length=15, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.id} - {self.name} - {self.email}"
    
class TypePlan(models.Model):
    type_plan = models.CharField(max_length=100)
    price = models.FloatField()
    duration = models.IntegerField()
    
    def __str__(self):
        return f"{self.id} - {self.type_plan} - {self.price} - {self.duration}"
    
class Payment(models.Model):
    amount = models.FloatField()
    date_payment = models.DateField(null=True, blank=True)
    date_end = models.DateField(null=True, blank=True)
    orders = models.ForeignKey('Orders', on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.id} - {self.amount} - {self.orders} - {self.date_payment}"
    
class Orders(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    type_plan = models.ForeignKey(TypePlan, on_delete=models.CASCADE)
    date = models.DateField(blank=True, auto_now_add=True)
    status = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    
    def __str__(self):
        return f"{self.id} - {self.client.name} - {self.type_plan.type_plan} - {self.date} - {self.status}"