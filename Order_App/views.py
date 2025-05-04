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

 
@login_required    
def cart_view(request):
   carts= Cart.objects.filter(user=request.user,purchased=False)
   orders= Order.objects.filter(user=request.user,ordered=False)
   
   if carts.exists() and orders.exists():
       order=orders[0]
       return render(request,"Order_App/cart.html",context={"carts":carts,"order":order}) 
   else:
       messages.warning(request,"you don't have anything in your cart")
       return redirect("Shop_App:home")    

@login_required
def remove_from_cart(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_qs = Order.objects.filter(user=request.user, ordered=False)

    if order_qs.exists():
        order = order_qs[0]

        if order.orderitems.filter(item=item).exists():
            order_item = Cart.objects.filter(item=item, user=request.user, purchased=False)[0]
            order.orderitems.remove(order_item)
            order_item.delete()
            messages.warning(request, "This item was removed from your cart")
            return redirect("Order_App:cart")
        else:
            messages.info(request, "This item was not in your cart.")
            return redirect("Shop_App:home")
    else:
        messages.info(request, "You don't have an active order")
        return redirect("Shop_App:home")