from rest_framework.test import APITestCase
from django.urls import reverse
from Boormag.models import Author, Library
from Boormag.serializers import BoormagSerializer, AuthorSerializer
from rest_framework import status


class BookAPITestCase(APITestCase):
    def test_get_list(self):
        library_1 = Library.objects.create(pk=1,name='Книга1', price=40, number_pages=340, date_publication='1945-07-13')
        library_2 = Library.objects.create(pk=2,name='Книга2', price=60, number_pages=340, date_publication='1945-07-13')
        url = reverse('api_library_list')

        print(url)
        print(library_1)
        print(library_2)

        response = self.client.get(url)

        serial_data = BoormagSerializer([library_1, library_2], many=True).data
        serial_data = {'librarys_list': serial_data}

        self.assertDictEqual(response.data, serial_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_list(self):
        # Создание и реализация на стороне приложения
        library_1 = Library(pk=1, name='Книга1', description='описание',  number_pages=340, sizes='А4', price=40, date_publication='1945-07-13', cover_type = 'картонная')
        serial_data = BoormagSerializer(library_1).data

        # Обращаемся к api-форме для сохранения объекта
        url = reverse('api_library_list')
        response = self.client.post(url, data={
            'pk':'1',
            'name':'Книга1',
            'description':'описание',
            'number_pages':'340',
             'price':'40',
             'sizes':'А4',
             'date_publication': '1945-07-13',
            'cover_type':'картонная',
        })


        self.assertDictEqual(response.data, serial_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class AuthorAPITestCase(APITestCase):
    def test_get_list(self):
        author_1 = Author.objects.create(pk=1,name2='автор1', firstname='Фамилия', lastname='Отчество', biograf='биография1', date_of_birth='1947-11-20', date_of_death='1947-11-20')
        author_2 = Author.objects.create(pk=2, name2='автор2', firstname='Фамилия', lastname='Отчество', biograf='биография1', date_of_birth='1947-11-20', date_of_death='1947-11-20')
        url = reverse('api_author_list')

        print(url)
        print(author_1)
        print(author_2)

        response = self.client.get(url)

        serial_data = AuthorSerializer([author_1, author_2], many=True).data
        serial_data = {'authors_list': serial_data}

        self.assertDictEqual(response.data, serial_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_list(self):
        # Создание и реализация на стороне приложения
        author_1 = Author(pk=1,name2='автор1', firstname='Фамилия', lastname='Отчество', biograf='биография1', date_of_birth='1947-11-20', date_of_death='1947-11-20')
        serial_data = AuthorSerializer(author_1).data

        # Обращаемся к api-форме для сохранения объекта
        url = reverse('api_author_list')
        response = self.client.post(url, data={
            'pk': '1',
            'name2':'автор1',
            'firstname':'Фамилия',
            'lastname':'Отчество',
            'biograf':'биография1',
            'date_of_birth':'1947-11-20',
             'date_of_death':'1947-11-20',
        })

        self.assertDictEqual(response.data, serial_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)