from django.contrib.auth import login
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView, ListView
# from ..forms import *
from ..forms import *
from ..models import *
from django.db.models import Q


class employee_home(ListView):
    model = Client
    template_name = 'employee/employee.html'


def order_list(request):
    orders = Order.objects.filter(order_date__lte=timezone.now(), order_status='Pending')
    return render(request, 'employee/orders_pending.html', {'orders': orders})


def order_processed(request):
    orders = Order.objects.filter(~Q(order_status='Pending'), order_date__lte=timezone.now())
    return render(request, 'employee/orders_processed.html', {'orders': orders})


def order_approve(request, id):
    orders = get_object_or_404(Order, id=id)
    orders.order_status = 'approved'
    orders.save()
    return redirect('employee:orders_pending')


def order_declined(request, id):
    orders = get_object_or_404(Order, id=id)
    orders.order_status = 'declined'
    orders.save()
    return redirect('employee:orders_pending')


def orders_pending_delete(request, id):
    drop = get_object_or_404(Order, id=id)
    drop.delete()
    return redirect('employee:orders_pending')


def orders_delete(request, id):
    drop = get_object_or_404(Order, id=id)
    drop.delete()
    return redirect('employee:order_processed')