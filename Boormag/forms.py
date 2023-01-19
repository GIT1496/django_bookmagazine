from django import forms
from .models import Library, Author

import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class BookForm(forms.ModelForm):
    class Meta:
        model = Library
        # fields = '__all__' # Использование всех полей (не реком.)
        fields = ['name', 'description', 'number_pages', 'price', 'sizes', 'cover_type','date_publication']

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'floatingInput',
                    'placeholder': 'Название книги'
                }
            ),
            'description': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Описание книги',
                }
            ),
            'number_pages': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Количество страниц в книге',
                }
            ),
            'price': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Цена книги',
                }
            ),

            'sizes': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Размер книги',
                }
            ),
            'cover_type': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Тип обложки',
                }
            ),
            'date_publication': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Дата публикации',
                }
            ),

        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if re.match(r'\d', name):
            raise ValidationError('Поле не должно начинаться с цифры')
        return name

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        # fields = '__all__' # Использование всех полей (не реком.)
        fields = ['name2', 'firstname', 'lastname', 'biograf','date_of_birth','date_of_death']
        widgets = {
            'name2': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'floatingInput',
                    'placeholder': 'Название книги'
                }
            ),
            'firstname': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Описание книги',
                }
            ),
            'lastname': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Количество страниц в книге',
                }
            ),
            'biograf': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Цена книги',
                }
            ),
            'date_of_birth': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Дата публикации',
                }
            ),
            'date_of_death': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Дата публикации',
                }
            ),
        }


def clean_name(self):
        name = self.cleaned_data['name2']
        if re.match(r'\d', name):
            raise ValidationError('Поле не должно начинаться с цифры')
        return name

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

class LoginForm(AuthenticationForm):
        username = forms.CharField(
            label='Логин',
            widget=forms.TextInput(attrs={'class': 'form-control'})
        )
        password = forms.CharField(
            label='Пароль',
            widget=forms.PasswordInput(attrs={'class': 'form-control'})
        )



    # Валидация
    # required=True - обязательное поле
    # max_length - максимальная длина текста
    # min_length - минимальная длина текста
    # max_value - максимальное значение числа
    # max_value - минимальное значение числа
    # step_size - шаг при установки числового значения

    # Стили
    # label - Вывод названия
    # widget - Указания типа поля
    # initial - Значение по умолчанию
    # help_text - подсказка под полем



# email
class ContactForm(forms.Form):
    recipient = forms.EmailField(
        label='Email',
        required=False,
        widget=forms.EmailInput(
            attrs={'class': 'form-control'}
        )
    )
    subject = forms.CharField(
        label='Тема письма',
        widget=forms.TextInput(
            attrs={'class':'form-control'}
        )
    )
    content = forms.CharField(
        label='Текст письма',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows': 8
            }
        )
    )

