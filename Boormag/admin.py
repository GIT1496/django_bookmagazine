from django.contrib import admin
from .models import Library, Author


class LibraryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')  # Отображение полей
    list_display_links = ('id', 'name')  # Установка ссылок на атрибуты
    search_fields = ('name', 'price')  # Поиск по полям

admin.site.register(Library, LibraryAdmin)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name2', 'firstname', 'lastname')  # Отображение полей
    list_display_links = ('id', 'name2')  # Установка ссылок на атрибуты
    search_fields = ('name2', 'firstname')

admin.site.register(Author, AuthorAdmin)









