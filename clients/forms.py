from django import forms
from .models import Client, TypePlan, Orders, Payment

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'address', 'phone','phone2']
        
class PlanForm(forms.ModelForm):
    class Meta:
        model = TypePlan
        fields = ['type_plan', 'price', 'duration']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['client', 'type_plan', 'status', 'address', 'phone']
        
class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['amount', 'date_payment', 'orders', 'status']