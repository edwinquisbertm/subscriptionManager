from django.urls import path
from . import views
    
urlpatterns = [
    path('', views.clients, name='clients'),
    path('details/<int:id>/', views.details, name='details'),
    path('orders/', views.orders, name='orders'),
    path('orders/order/<int:id>/', views.details_order, name='order'),
    path('plans/', views.list_plan, name='plans'),
    path('payments/', views.list_payment, name='payments'),
]