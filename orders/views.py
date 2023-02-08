from django.shortcuts import render
from .models import Order, OrderItem
from .forms import OrderCreateForm
from .forms import OrderStatusForm
from basket.basket import Basket
from django.views.generic import TemplateView, ListView
from django.db.models import Q


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

class HomePageView(TemplateView):
    template_name = 'library/search/home.html'


class SearchResultsView(ListView):
    model = Order, OrderItem
    template_name = 'library/search/search_results.html'

    def get_queryset(self):  # новый
        query = self.request.GET.get('q')
        object_list = Order.objects.filter(
            Q(id__icontains=query) | Q(status__icontains=query)
        )
        return object_list










