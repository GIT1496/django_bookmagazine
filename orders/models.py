from django.db import models
from Boormag.models import Library

class Order(models.Model):
    first_name = models.CharField(verbose_name='Фамилия', max_length=50)
    last_name = models.CharField(verbose_name='Отчество', max_length=50)
    name = models.CharField(verbose_name='Имя', null=True, max_length=50)
    email = models.EmailField(verbose_name='Email')
    address = models.CharField(verbose_name='Адрес', max_length=250)
    postal_code = models.CharField(verbose_name='Индекс', max_length=20)
    city = models.CharField(verbose_name='Город', max_length=100)
    created = models.DateTimeField(verbose_name='Дата создания заказа', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Дата изменения заказа', auto_now=True)
    paid = models.BooleanField(verbose_name='Оплачен', default=False)
    status = models.CharField(max_length=150, null=True, verbose_name='Статус',
                              choices=[
                                  ('Создан', 'Создан'),
                                  ('Отменён', 'Отменён'),
                                  ('Согласован', 'Согласован'),
                                  ('В пути', 'В пути'),
                                  ('Завершён', 'Завершён'),
                              ]
                              )

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'



    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, verbose_name='Заказ', related_name='items', null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Library, verbose_name='Книга', related_name='order_items', null=True, on_delete=models.SET_NULL)
    price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2)
    count_prod = models.PositiveIntegerField(verbose_name='Количество книг', default=1)


    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.count_prod



# class Order_status(models.Model):
#     date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа')
#     date_finish = models.DateTimeField(null=True, blank=True, verbose_name='Дата завершения заказа')
#     price = models.FloatField(null=True, verbose_name='Стоимость заказ')
#     address_delivery = models.CharField(max_length=150, verbose_name='Адрес доставки')
#     paid = models.BooleanField(verbose_name='Оплачен', default=False)
#
#
#     orders = models.ManyToManyField(Order, through='Pos_order')
#
# class Pos_order(models.Model):
#     order = models.ForeignKey(OrderItem, on_delete=models.PROTECT, verbose_name='Заказ')
#     order_status = models.ForeignKey(Order_status, on_delete=models.PROTECT, verbose_name='Статус заказа')
#     price = models.FloatField(verbose_name='Общая цена книг')
#
#     def __str__(self):
#         return self.fruit.name + " " + self.order.address_delivery + " " + self.order.status
#
#     class Meta:  # Класс для названий нашей модели в админке
#         verbose_name = 'Позиция'  # Надпись в единственном числе
#         verbose_name_plural = 'Позиции'  # Надпись во множественном числе
#         ordering = ['fruit', 'order', 'price']  # Сортировка полей (по возрастанию)




# Create your models here.
