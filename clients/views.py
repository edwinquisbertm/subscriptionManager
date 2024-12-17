from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .forms import ClientForm, PlanForm, OrderForm, PaymentForm
from .models import Client, Orders, TypePlan, Payment

def home(request):
  template = loader.get_template('home.html')
  context = {}
  return HttpResponse(template.render(context, request))

def clients(request):
  myclients = Client.objects.all().values()
  template = loader.get_template('clients.html')
  context = {
    'myclients': myclients,
  }
  return HttpResponse(template.render(context, request))

def list_plan(request):
  plan_list = TypePlan.objects.all().values()
  template = loader.get_template('plans.html')
  context = {
    'plan_list': plan_list,
  }
  return HttpResponse(template.render(context, request))

def orders(request):
  orders_list = Orders.objects.select_related('client', 'type_plan').all()
  template = loader.get_template('orders.html')
  context = {
    'orders_list': orders_list,
  }
  return HttpResponse(template.render(context, request))


def details(request, id):
  myclient = Client.objects.get(id=id)
  template = loader.get_template('details_client.html')
  context = {
    'myclient': myclient,
  }
  return HttpResponse(template.render(context, request))

def details_order(request, id):
  myorder = Orders.objects.get(id=id)
  template = loader.get_template('details_order.html')
  context = {
    'myorder': myorder,
  }
  return HttpResponse(template.render(context, request))

def list_payment(request):
  payment_list = Payment.objects.select_related('orders').all()
  template = loader.get_template('payments.html')
  context = {
    'payment_list': payment_list,
  }
  return HttpResponse(template.render(context, request))

def create_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clients')
    else:
        form = ClientForm()
    return render(request, 'create_client.html', {'form': form})

def create_plan(request):
    if request.method == 'POST':
        form = PlanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('plans')
    else:
        form = PlanForm()
    return render(request, 'create_plan.html', {'form': form})

def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('orders')
    else:
        form = OrderForm()
    clients = Client.objects.all()
    plans = TypePlan.objects.all()
    return render(request, 'create_order.html', {'form': form, 'clients': clients, 'plans': plans})

def create_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payments')
    else:
        form = PaymentForm()
    orders = Orders.objects.all()
    return render(request, 'create_payment.html', {'form': form, 'orders': orders})