from django.conf import settings
from Boormag.models import Library

class Basket:
    def __init__(self, request):
        self.session = request.session
        basket = self.session.get(settings.BASKET_SESSION_ID)

        if not basket:
            basket = self.session[settings.BASKET_SESSION_ID] = {}

        # SESSION = {
        #     'basket': {}
        # }
        self.basket = basket

    def save(self):
        # Обновление ключа "basket" в сессии
        self.session[settings.BASKET_SESSION_ID] = self.basket
        # Отметка сессии в опции "измененный", для обновления и сохранения данных
        self.session.modified = True

    def add(self, product, count_product=1, update_count=False):
        prod_pk = str(product.pk)

        # Проверка наличия продукта в корзине (если нет в корзине, то добавляем)
        if prod_pk not in self.basket:
            self.basket[prod_pk] = {
                'count_prod': 0,
                'price_prod': str(product.price)
            }
        # SESSION = {
        #     'basket': {
        #       '1' : {
        #           'count_prod':'16',
        #           'price_prod':'123.92'
        #             },
        #       '2' : {
        #           'count_prod': '0',
        #           'price_prod':'83.54'
        #             },
        #       }
        # }

        # Обновление количества продукта в корзине
        if update_count:
            self.basket[prod_pk]['count_prod'] = count_product
        else:
            self.basket[prod_pk]['count_prod'] += count_product

        # SESSION = {
        #     'basket': {
        #       '1' : {
        #           'count_prod':'16',
        #           'price_prod':'123.92'
        #             },
        #       '2' : {
        #           'count_prod': '9',
        #           'price_prod':'83.54'
        #             },
        #       }
        # }

        # Сохранение корзины в сессию
        self.save()

    def remove(self, product):
        prod_pk = str(product.pk)

        # Если удаляемый товар лежит в корзине, то очищаем его ключ (и данные о нём)
        if prod_pk in self.basket:

            # prod_pk = 2
            # SESSION = {
            #     'basket': {
            #       '1' : {
            #           'count_prod':'16',
            #           'price_prod':'123.92'
            #             },
            #       '2' : {
            #           'count_prod': '0',
            #           'price_prod':'83.54'
            #             },
            #       }
            # }

            del self.basket[prod_pk]

            # SESSION = {
            #     'basket': {
            #       '1' : {
            #           'count_prod':'16',
            #           'price_prod':'123.92'
            #             },
            #       }
            # }
            self.save()

    def get_total_full_price(self):
        # sum_price = 0
        # for item in self.basket.values():
        #     sum_price += float(item['price_prod']) * int(item['count_prod'])
        # return sum_price
        # ==
        return round(sum(float(item['price_prod']) * int(item['count_prod']) for item in self.basket.values()), 2)

        # SESSION = {
        #     'basket': {
        #       '1' : {
        #           'count_prod':'16',
        #           'price_prod':'123.92'
        #             },
        #       '2' : {
        #           'count_prod': '9',
        #           'price_prod':'83.54'
        #             },
        #       }
        # }

    def clear(self):

        # SESSION = {
        #     'basket': {
        #       '1' : {
        #           'count_prod':'16',
        #           'price_prod':'123.92'
        #             },
        #       '2' : {
        #           'count_prod': '0',
        #           'price_prod':'83.54'
        #             },
        #       }
        # }

        del self.session[settings.BASKET_SESSION_ID]

        # SESSION = {}
        # ==
        # del self.basket
        self.session.modified = True

    def __len__(self):
        return sum(int(item['count_prod']) for item in self.basket.values())

    def __iter__(self):
        # Получение первичных ключей
        list_prod_pk = self.basket.keys()

        # Загрузка данных из БД
        list_prod_obj = Library.objects.filter(pk__in=list_prod_pk)

        # Копирование корзины для дальнейшей работы
        basket = self.basket.copy()
        # Перебор и добавление объектов(записей) из БД
        for prod_obj in list_prod_obj:
            basket[str(prod_obj.pk)]['library'] = prod_obj

            #     'basket': {
            #       '1' : {
            #           'count_prod':'16',
            #           'price_prod':'123.92',
            #           'fruit': prod_obj
            #             },
            #       '2' : {
            #           'count_prod': '0',
            #           'price_prod':'83.54',
            #           'fruit': prod_obj
            #             },
            #       }

        for item in basket.values():
            item['total_price'] = round(float(item['price_prod']) * int(item['count_prod']),2)

            #     'basket': {
            #       '1' : {
            #           'count_prod':'16',
            #           'price_prod':'123.92',
            #           'fruit': prod_obj,
            #           'total_price':'1283.94'
            #             },
            #       '2' : {
            #           'count_prod': '0',
            #           'price_prod':'83.54',
            #           'fruit': prod_obj,
            #           'total_price':'1283.94'
            #             },
            #       }

            yield item