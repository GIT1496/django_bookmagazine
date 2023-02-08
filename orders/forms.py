from django import forms
from .models import Order
from .models import OrderItem


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'name', 'last_name', 'email', 'address', 'postal_code', 'city']
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'floatingInput',
                    'placeholder': 'Фамилия'
                }
            ),
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Имя'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Отчество',
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Email',
                }
            ),
            'address': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Адрес доставки',
                }
            ),

            'postal_code': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Индекс',
                }
            ),
            'city': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Город доставки',
                }
            ),
        }

class OrderStatusForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['order']

        widgets = {
            'order': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'floatingInput',
                    'placeholder': 'Номер заказа'
                }
            ),
        }
