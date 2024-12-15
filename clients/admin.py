from django.contrib import admin
from .models import Client, TypePlan, Payment

admin.site.register(Client)
admin.site.register(TypePlan)
admin.site.register(Payment)