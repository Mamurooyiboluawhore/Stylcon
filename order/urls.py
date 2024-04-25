from django.urls import path
from .views import OrderList, OrderDetailViews


urlpatterns = [
    path('', OrderList.as_view(), name='List of Order'),
    path('create-order/', OrderDetailViews.as_view(), name='create-order')
]