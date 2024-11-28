from django.shortcuts import get_object_or_404
from .models import Book, Order
import os
from django.conf import settings
from django.shortcuts import render, redirect
from .forms import OrderForm


def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'basket/order_form.html', {'form': form})  


def order_list(request):
    orders = Order.objects.all()
    template_path = os.path.join(settings.BASE_DIR, 'basket', 'templates', 'basket', 'order_list.html')
    if not os.path.exists(template_path):
        return HttpResponse(f"Template not found at {template_path}")
    return render(request, 'basket/order_list.html', {'orders': orders})


def order_edit(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            old_book = order.book
            old_book.increase_quantity()
            new_order = form.save()
            new_order.book.decrease_quantity()
            return redirect('order_list')
    else:
        form = OrderForm(instance=order)
    return render(request, 'orders/order_form.html', {'form': form})


def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        order.book.increase_quantity()
        order.delete()
        return redirect('order_list')
    return render(request, 'orders/order_confirm_delete.html', {'order': order})


