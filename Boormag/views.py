from django.http import HttpResponse, HttpResponseRedirect
from .models import Library, Author
from .forms import BookForm, AuthorForm
from .util import Default_value
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from .forms import RegistrationForm, LoginForm



from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator

from django.contrib import messages

from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings


# API
from .serializers import BoormagSerializer, AuthorSerializer


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets


def index_template(request):
        return render(request, 'library/index.html')

def request_info(request):
        if request.GET.get("META") == "TRUE":
            meta_output = ""
            for key, value in request.META.items():
                meta_output += f'{key}: {value}<br>'
            return HttpResponse(meta_output)
        return render(request, 'info/request.html', {'req_item': request})

# Книги
class BookListView(ListView, Default_value):  # Возврат листа объектов
    model = Library # определение таблицы для взаимодействия
    template_name = 'library/library_All.html'  # путь шаблона (<Имя приложения>/<Имя модели>_list.html)
    context_object_name = 'Library'  # Отправка данных по заданному ключу (object_list)
    extra_context = {'title': 'Список книг из класса'}  # Доп. значения (статичные данные)


    paginate_by = 2

# Авторы
class AutorListView(ListView, Default_value):  # Возврат листа объектов
    model = Author # определение таблицы для взаимодействия
    template_name = 'library/Author/Author-list.html'  # путь шаблона (<Имя приложения>/<Имя модели>_list.html)
    context_object_name = 'Author'  # Отправка данных по заданному ключу (object_list)
    extra_context = {'title': 'Список авторов из класса'}  # Доп. значения (статичные данные)

    def get_context_data(self, *args, **kwargs):
        wiki_list = Author.objects.order_by('name2')
        context = super(AutorListView, self).get_context_data(*args, **kwargs)
        context["wiki_list"] = wiki_list
        return context


    paginate_by = 2

# Книги

class BookDetailView(DetailView):
    model = Library
    template_name = 'library/library_info.html'
    context_object_name = 'one_library'  # (object)
    pk_url_kwarg = 'library_id'
    allow_empty = False  # Возврат 404 при отсутствии данных


# Авторы
class AuthorDetailView(DetailView):
    model = Author
    template_name = 'library/Author/Author-info.html'
    context_object_name = 'object'  # (object)
    pk_url_kwarg = 'object_id'  # Переопределение ключа ID при получении (pk)
    allow_empty = False  # Возврат 404 при отсутствии данных

# Книги

class BookCreateView(CreateView):
    model = Library
    form_class = BookForm  # Определение формы для взаимодействия
    template_name = 'library/library_add.html'
    context_object_name = 'form'  # Переопределение ключа формы (object)
    success_url = reverse_lazy('list_lib_view')


# def author_add(request):
#     if request.method == "POST":
#         context = dict()
#         context['name2'] = request.POST.get('name2')
#         context['firstname'] = request.POST.get('firstname')
#         context['lastname'] = request.POST.get('lastname')
#         context['biograf'] = request.POST.get('biograf')
#         context['photo'] = request.POST.get('photo')
#         context['date_of_birth'] = request.POST.get('date_of_birth')
#         context['date_of_death'] = request.POST.get('date_of_death')
#         context['librarys'] = request.POST.get('librarys')
#
#
#         return HttpResponseRedirect('list_lib_view')
#     else:
#         authorform = AuthorForm()
#         context = {'form': authorform}
#         return render(request, 'library/Author/Author-add.html', context=context)


# Авторы
class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm  # Определение формы для взаимодействия
    template_name = 'library/Author/Author-add.html'
    context_object_name = 'form'  # Переопределение ключа формы (object)
    success_url = reverse_lazy('list_author_view')

    # success_url = '/fruit/supplier/view/list'

    # Права доступа
    @method_decorator(permission_required('Boormag.add_Author'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

# Книги

class BookUpdateView(UpdateView):
    model = Library
    form_class = BookForm
    template_name = 'library/library-edit.html'
    context_object_name = 'form'

    # Права доступа
    @method_decorator(permission_required('Boormag.change_Library'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

# Авторы
class AuthorUpdateView(UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = 'library/Author/Author-edit.html'
    context_object_name = 'form'
    success_url = reverse_lazy('list_author_view')

    # Права доступа
    @method_decorator(permission_required('Boormag.change_Author'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


# Книги
class BookDeleteView(DeleteView):
    model = Library
    success_url = reverse_lazy('list_lib_view')
    template_name = 'library/library-delet..html'

    # Права доступа
    @method_decorator(permission_required('Boormag.delete_Library'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


# Авторы
class AuthorDeleteView(DeleteView):
    model = Author
    success_url = reverse_lazy('list_author_view')
    template_name = 'library/Author/Author-delete.html'

    # Права доступа
    @method_decorator(permission_required('Boormag.delete_Library'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

# регистрация
def user_registration(request):
    if request.method == "POST":
        # form = UserCreationForm(request.POST) # Форма создания пользователя из auth
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Запись нового пользователя
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('login')
        else:
            messages.error(request, 'Не удалось зарегистрировать')
    else:
        # form = UserCreationForm()
        form = RegistrationForm()
    return render(request, 'library/auth/registration.html', {'form': form})
#
#Авторизация
def user_login(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            print(user)
            print(request.user.is_authenticated)
            print(request.user.is_anonymous)
            login(request, user)
            print(request.user.is_authenticated)
            print(request.user.is_anonymous)
            messages.success(request, 'Вы успешно авторизовались')
            return redirect('list_lib_view')
        messages.error(request, 'Авторизация прошла с ошибкой, перепроверьте логин и/или пароль')
    else:
        form = LoginForm()
    return render(request, 'library/auth/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')

# Права пользователя
def is_login(request):
    if request.user.is_anonymous:
        return HttpResponse('<h1>Вы аноним</h1>')
    else:
        return HttpResponse('<h1>Зарегистрированы</h1>')


@login_required
def is_login_decorator(request):
    return HttpResponse('<h1>Зарегистрированы</h1>')


def is_permession(request):
    text = ''
    if request.user.has_perm('Boormag.add_Library'):  # <Название приложения>.<операция>_<название модели>
        text += '<h1>Вы можете добавлять книги</h1>'
    if request.user.has_perm('Boormag.change_Library'):
        text += '<h1>Вы можете изменять книги</h1>'
    if request.user.has_perm('Boormag.view_Library'):
        text += '<h1>Вы можете просматривать книги</h1>'
    if text == '':
        HttpResponse('<h1>У вас нет прав</h1>')
    return HttpResponse(text)


@permission_required('Boormag.add_Library')
def is_perm_add(request):
    return HttpResponse('<h1>Добавление книги</h1>')


@permission_required('Boormag.change_Library')
def is_perm_change(request):
    return HttpResponse('<h1>Изменение книг</h1>')


@permission_required(['Boormag.change_supplier', 'Boormag.view_Library'])
def is_perm_change_view(request):
    return HttpResponse('<h1>Изменение и просмотр книг</h1>')

# Вывод ошибок
def error_404(request, exception):
    context = dict()
    context['title'] = 'Упс, вы попали куда-то не туда'
    response = render(request, 'library/error/404.html')
    response.status_code = 404
    return response

def error_400(request, exception):
    context = dict()
    context['title'] = 'неправильный, некорректный запрос'
    response = render(request, 'library/error/400.html')
    response.status_code = 400
    return response

def error_403(request, exception):
    context = dict()
    context['title'] = 'запрещено (не уполномочен)'
    response = render(request, 'library/error/403.html')
    response.status_code = 403
    return response

def error_500(request, exception):
    context = dict()
    context['title'] = 'внутренняя ошибка сервера'
    response = render(request, 'library/error/500.html')
    response.status_code = 500
    return response

#email
def send_contact_email(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            mail = send_mail(  # Отправка письма
                form.cleaned_data['subject'],  # Заголовок письма
                form.cleaned_data['content'],  # Тело письма
                settings.EMAIL_HOST_USER,  # Отправитель письмо
                (['django1496@mail.ru']),
                fail_silently=False,  # Режим отображения ошибок (True - исключения не будет)
                #                               (False - исключения выведутся на страницу)
            )
            if mail:
                messages.success(request, 'Письмо было успешно отправлено')
                return redirect('list_lib_view')
            else:
                messages.error(request, 'Письмо не удалось успешно отправить')
        else:
            messages.error(request, 'Письмо заполнено неверно')
    else:
        form = ContactForm()
    return render(request, 'library/other/contact.html', {'title': 'Предложения и пожелания', 'form': form})


# API книги
@api_view(['GET', 'POST'])
def library_api_list(request, format=None):
    if request.method == "GET":
        librarys = Library.objects.all()
        serializer = BoormagSerializer(librarys, many=True)
        return Response({'librarys_list': serializer.data})
        # return JsonResponse({'fruits_list': serializer.data})
        # return JsonResponse(serializer.data, safe=False)
    if request.method == "POST":
        serializer = BoormagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def library_api_detail(request, pk, format=None):
    library_obj = get_object_or_404(Library, pk=pk)

    if request.method == 'GET':
        serializer = BoormagSerializer(library_obj)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = BoormagSerializer(library_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        library_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




# API авторы
@api_view(['GET', 'POST'])
def author_api_list(request, format=None):
    if request.method == "GET":
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response({'authors_list': serializer.data})
        # return JsonResponse({'fruits_list': serializer.data})
        # return JsonResponse(serializer.data, safe=False)
    if request.method == "POST":
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def author_api_detail(request, pk, format=None):
    author_obj = get_object_or_404(Author, pk=pk)

    if request.method == 'GET':
        serializer = AuthorSerializer(author_obj)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = AuthorSerializer(author_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        author_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# SESSION
def set_session_info(request):
    request.session['test_session'] = 'Привет сессии'
    return HttpResponse('Задали значение в сессии: ' + request.session.get('test_session'))


def get_session_info(request):
    return HttpResponse(request.session.get('test_session'))


def get_session_info_full(request):
    return HttpResponse(request.session.items())