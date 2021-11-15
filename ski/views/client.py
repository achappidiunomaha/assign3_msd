from django.contrib.auth import login
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView, ListView
from ..forms import *
from ..models import *
from django.contrib.auth.forms import PasswordChangeForm
from django.db.models import Q


class ClientSignUpView(CreateView):
    model = User
    form_class = ClientSignUpForm
    template_name = 'registration/signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'client'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        form.save()
        return redirect('home')


class client_home(ListView):
    model = Client
    template_name = 'client/client.html'


def equipmentall(request):
    products = Product.objects.all()
    return render(request, 'client/equipment.html', {'products': products})


def equipmentdetail(request, id):
    products = get_object_or_404(Product, id=id)
    return render(request, 'client/equipment_detail.html', {'products': products})


def order_checkout(request, id):
    product = get_object_or_404(Product, id=id)
    user = request.user
    Order.objects.create(product=product, user=user)
    return render(request, 'client/checkout.html', {'products': product})


def client_details(request):
    current_user = request.user
    client = Client.objects.get(user_id=current_user.id)
    return render(request, 'client/account.html', {'client': client})


def client_edit(request):
    if request.method == "POST":
        user_form = UserForm(request.POST, instance=request.user)
        client_form = ClientForm(request.POST, instance=request.user.client)
        if user_form.is_valid() and client_form.is_valid():
            user_form.save()
            client_form.save()
            current_user = request.user
            client = Client.objects.get(user_id=current_user.id)
            return render(request, 'client/account.html', {'client': client})
    else:
        user_form = UserForm(instance=request.user)
        client_form = ClientForm(instance=request.user.client)
        return render(request, 'client/account_edit.html', {'user_form': user_form, 'client_form': client_form})


def orders(request):
    current_user = request.user
    orders = Order.objects.filter(~Q(order_status='Pending'), user_id=current_user.id, )
    return render(request, 'client/orders.html', {'orders': orders})


def orders_pending(request):
    current_user = request.user
    orders = Order.objects.filter(Q(order_status='Pending'), user_id=current_user.id)
    return render(request, 'client/orders_pending.html', {'orders': orders})


def orders_delete(request, id):
    drop = get_object_or_404(Order, id=id)
    drop.delete()
    return redirect('client:orders')


def orders_pending_delete(request, id):
    drop = get_object_or_404(Order, id=id)
    drop.delete()
    return redirect('client:orders_pending')
