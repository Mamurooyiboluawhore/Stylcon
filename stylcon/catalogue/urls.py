from django.urls import include, path
from .views import CatalogueAPIViews



urlpatterns = [
    path('', CatalogueAPIViews.as_view(), name='catalogue-list'),
    path('create-catalgue/', CatalogueAPIViews.as_view(), name='create-catalogue')
]