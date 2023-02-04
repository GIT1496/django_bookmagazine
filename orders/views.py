from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from basket.basket import Basket


def order_create(request):
    basket = Basket(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in basket:
                OrderItem.objects.create(order=order,
                                         product=item['library'],
                                         price=item['price_prod'],
                                         count_prod=item['count_prod'])
            # очистка корзины
            basket.clear()
            return render(request, 'orders/order/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'orders/order/create.html',
                  {'basket': basket, 'form': form})


# Create your views here.
