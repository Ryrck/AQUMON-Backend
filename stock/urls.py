from django.conf.urls import url
from . import views

urlpatterns = [
    url('stock_api', views.stock_api),
    url('get_stock', views.get_stock),
    url('clear_table', views.clear_table),
    url('delete_stock', views.delete_stock),
    url('add_stock', views.add_stock),
]