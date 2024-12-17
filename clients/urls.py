from django.urls import path
from . import views
    
urlpatterns = [
    path('', views.home, name='home'),
    path('clients/', views.clients, name='clients'),
    path('details/<int:id>/', views.details, name='details'),
    path('orders/', views.orders, name='orders'),
    path('orders/order/<int:id>/', views.details_order, name='order'),
    path('plans/', views.list_plan, name='plans'),
    path('payments/', views.list_payment, name='payments'),
    path('add-client/', views.create_client, name='add_client'),
    path('add-plan/', views.create_plan, name='add_plan'),
    path('add-order/', views.create_order, name='add_order'),
    path('add-payment/', views.create_payment, name='add_payment'),
]