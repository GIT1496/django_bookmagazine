from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns


from Boormag.views import *

urlpatterns = [
    path('', index_template, name='index_library'),
    # path('list/',library_template, name='list_library'),
    path('library/view/All/', BookListView.as_view(), name='list_lib_view'),
    path('library/view/<int:library_id>', BookDetailView.as_view(), name='info_lib_view'),
    # path('list/<int:library_id>/', library_detail, name='one_library'),
    path ('library/view/add/', BookCreateView.as_view(), name='add_lib_view'),
    path('library/view/edit/<int:pk>', BookUpdateView.as_view(), name='edit_lib_view'),
    path('library/view/delete/<int:pk>', BookDeleteView.as_view(), name='delete_library_view'),
    path('login/', user_login, name='login'),
    path('registration/', user_registration, name='registration'),
    path('logout/', user_logout, name='logout'),
    path('info', AutorListView.as_view(), name='list_author_view'),
    path('author/view/<int:object_id>', AuthorDetailView.as_view(), name='info_author_view'),
    path('author/view/add/', AuthorCreateView.as_view(), name='add_author_view'),
    # path('add/', author_add, name='add_author'),
    path('author/view/edit/<int:pk>', AuthorUpdateView.as_view(), name='edit_author_view'),
    path('author/view/delete/<int:pk>', AuthorDeleteView.as_view(), name='delete_author_view'),

    path('is_login/', is_login),
    path('is_login_decorator/', is_login_decorator),

    path('is_perm/', is_permession),
    path('is_perm_add/', is_perm_add),
    path('is_perm_change/', is_perm_change),
    path('is_perm_change_view/', is_perm_change_view),

    # path('add/', library_add, name='add_library'),
    path('info/', request_info),

    #email
    path('contact/', send_contact_email, name='send_contact'),

    # API
    path('api/library/', library_api_list, name='api_library_list'),
    path('api/library/<int:pk>', library_api_detail, name='api_library_detail'),
    path('api/author/', author_api_list, name='api_author_list'),
    path('api/author/<int:pk>', author_api_detail, name='api_author_detail'),

    path('session/set', set_session_info),
    path('session/get', get_session_info),
    path('session/get-full', get_session_info_full),
]

urlpatterns = format_suffix_patterns(urlpatterns)