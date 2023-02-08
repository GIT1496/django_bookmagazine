from django.urls import path
from .import views
from orders.views import *


urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('', HomePageView.as_view(), name='home'),
]
