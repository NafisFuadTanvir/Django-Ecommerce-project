from django.shortcuts import render,get_object_or_404,redirect

#for authentication
from django.contrib.auth.decorators import login_required

#models
from .models import Cart,Order
from Shop_App.models import Product

from django.contrib import messages

@login_required
def add_to_cart(request, pk):
    item = get_object_or_404(Product, pk=pk)

    order_item = Cart.objects.get_or_create(
        item=item,
        user=request.user,
        purchased=False
    )

    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )

    if order_qs.exists():
        order = order_qs[0]

        if order.orderitems.filter(item=item).exists():
            order_item[0].quantity += 1
            order_item[0].save()
            messages.info(request, "This item quantity was updated.")
            return redirect('Shop_App:home')
        else:
            order.orderitems.add(order_item[0])
            messages.info(request, "This item was added to your cart.")
            return redirect('Shop_App:home')
    else:
        order = Order.objects.create(
            user=request.user,
            ordered=False
        )
        order.save()
        order.orderitems.add(order_item[0])
        messages.info(request, "This item was added to your cart.")
        return redirect('Shop_App:home')

    
    
