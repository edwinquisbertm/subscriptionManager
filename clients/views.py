from django.http import HttpResponse
from django.template import loader
from .models import Client, Orders

def clients(request):
  myclients = Client.objects.all().values()
  template = loader.get_template('clients.html')
  context = {
    'myclients': myclients,
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