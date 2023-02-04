from django.db import models
from django.urls import reverse, reverse_lazy

class Library(models.Model):
    name = models.CharField(max_length=120, null=True, default='library', verbose_name='Название книги')
    description = models.TextField(blank=True, null=False, verbose_name='Описание книги')
    number_pages = models.IntegerField(null=False, verbose_name='Количество страниц в книге')
    price = models.FloatField(null=True, verbose_name='Цена книги')
    sizes = models.TextField(null=False, verbose_name='Размер книги')
    date_publication = models.DateField(null=False, verbose_name='Дата публикации книги')
    cover_type = models.TextField (blank=True, null=True, verbose_name='Тип обожки книги')
    photo = models.ImageField(upload_to='image/%Y/%m/%d', null=True, verbose_name='Фотография книги')
    authors = models.ForeignKey('Author', on_delete=models.DO_NOTHING, null=True, verbose_name='Автор книги')

    def get_absolute_url(self):  # тэг url для объекта (Данный метод для вывода странички одной записи)
        return reverse('one_library', kwargs={'library_id': self.pk})

    def __str__(self):
        return self.name


    class Meta:  # Класс для названий нашей модели в админке
        verbose_name = 'Книгу'  # Надпись в единственном числе
        verbose_name_plural = 'Книги'  # Надпись во множественном числе
        ordering = ['name']  # Сортировка полей (по возрастанию)

class Author(models.Model):
    name2 = models.CharField(max_length=120, null=True, verbose_name='Имя автора')
    firstname = models.CharField(max_length=120, null=True, verbose_name='Фамилия автора')
    lastname = models.CharField(max_length=120, null=True, verbose_name='Отчество автора')
    biograf = models.TextField(blank=True, null=False, verbose_name='Биография автора')
    photo = models.ImageField(upload_to='image/%Y/%m/%d', null=True, verbose_name='Портрет автора')
    date_of_birth = models.DateField(null=True, verbose_name='Дата рождения автора')
    date_of_death = models.TextField(null=True, verbose_name='Дата смерти автора')
    librarys = models.TextField(null=True,
                                 verbose_name='Написаннные книги')

    def get_absolute_url(self):  # тэг url для объекта (Данный метод для вывода странички одной записи)
        return reverse('info_author_view', kwargs={'author_id': self.pk})



    def __str__(self):
        return self.name2 + " " + self.firstname + " " + self.lastname

    class Meta:  # Класс для названий нашей модели в админке
        verbose_name = 'Автор книги'  # Надпись в единственном числе
        verbose_name_plural = 'Авторы книг'  # Надпись во множественном числе










